from django import forms

from .models import Countres, Auto

class CountresForm(forms.ModelForm):
	class Meta:
		model = Countres
		fields = ['country']
		labels = {'text': 'Введите страну'}

class AutoForm(forms.ModelForm):
	class Meta:
		model = Auto
		fields = ['auto']
		labels = {'text': 'Введите названия Авто'}