from django.urls import path, re_path

from .views import *

app_name = 'car'

urlpatterns = [
	path('', countres, name='countres_url'),
	path('country/<int:country_id>/', cars, name='cars_url'),
	path('new_countres', new_countres, name='new_countres_url'),
	path('new_auto/<int:country_id>/', new_cars, name='new_cars_url'),
	path('edit_auto/<int:auto_id>/', edit_auto, name='edit_auto_url'),

]