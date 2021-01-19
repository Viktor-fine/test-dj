from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
#from django.urls import reverse

from .models import Countres, Auto
from .forms import CountresForm, AutoForm



def countres(request):
	""" Выводит список стран из БД """
	countres = Countres.objects.all()
	context = {'strana': countres}
	return render(request, 'car/countres.html', context)


@login_required
def cars(request, country_id):
	""" Выводит список автомобилей производимых в выбранной стране """
	country = Countres.objects.get(id=country_id)
	autos = country.auto_set.all()
	context = {'strana': country, 'auto': autos}
	return render(request, 'car/cars.html', context)

def new_countres(request):
	""" определяет новую тему """
	if request.method != 'POST':
		#создаётся пустая форма, при первой загрузки страницы(это происходит методом GET)
		forma = CountresForm()
	else:
		#Пользователь ввёл свои данные(метод POST). Проверить их.
		forma = CountresForm(request.POST) #Тут находятся данные введённые пользователем
		if forma.is_valid():
			forma.save()
			return HttpResponseRedirect(reverse('car:countres_url'))
	context ={'form': forma}
	return render(request, 'car/new_countres.html', context)



def new_cars(request, country_id):
	""" Добавляет новую марку Автомобиля для конкретной страны """
	country = Countres.objects.get(id=country_id)
	if request.method != 'POST':
		# при первой загрузки отрисовать пустую форму
		form = AutoForm()
	else:
		#отправленны данные методом POST. Обработать данные
		form = AutoForm(data=request.POST)
		if form.is_valid():
			new_auto = form.save(commit=False)
			new_auto.fore = country
			new_auto.save()
			return redirect('car:cars_url', country_id = country_id)
	context = {'country': country, 'form': form}
	return render(request, 'car/new_auto.html', context)



def edit_auto(request, auto_id):
	# Редактирует существующую запись
	auto = Auto.objects.get(id=auto_id)
	country = auto.fore

	if request.method != 'POST':
		#Исходный запрос, форма заполняется имеющимися данными
		form = AutoForm(instance=auto)
	else:
		#Отправка данных POST, обработать данные
		form = AutoForm(instance=auto, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('car:cars_url', country_id=country.id)
	context={'car': auto, 'country': country, 'form': form}
	return render(request, 'car/edit_auto.html', context)


