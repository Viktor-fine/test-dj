""" Определяет схемы URL для пользователей(приложение Users) """

from django.urls import path, include

from .views import *

app_name = 'users'

urlpatterns = [
	#Включить URL авторизации по умолчанию.
	path('', include('django.contrib.auth.urls')), #Включает именнованные схемы такие как 'login' и 'logaut'
	path('register/', register, name='register'),
]