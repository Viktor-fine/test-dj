from django.db import models

class Countres(models.Model):
	""" Страна где производят автомобиль """
	country = models.CharField(max_length=20, unique=True, verbose_name="Страна")
	date_add = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural="Страна производитель"

	def __str__(self):
		""" Возвращает строковое представление модели """
		return self.country


class Auto(models.Model):
	fore = models.ForeignKey(Countres, on_delete=models.CASCADE)
	auto = models.CharField(max_length=20, unique=True, verbose_name="Название модели")
	date_add = models.DateTimeField(auto_now_add=True)
	text = models.TextField(default='', verbose_name="Описание")


	class Meta:
		verbose_name_plural="Название марки"

	def __str__(self):
		""" Возвращает строковое представление модели """
		return self.auto


