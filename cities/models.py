from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Город')

    def __str__(self):
        return self.name

    class Meta:
        # Читабельное название модели.
        verbose_name = 'Город'
        # Читабельное название модели во множественном числе.
        verbose_name_plural = 'Города'
        # Сортировка объектов по полю 'name' по возрастанию.
        # Сортировка по убыванию ordering = ['-name']
        ordering = ['name']

