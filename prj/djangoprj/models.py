from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name= 'Название')
    descriptions = models.TextField(null=True, blank=True, verbose_name= 'Описание')  # поле может быть пустым

    def __str__(self):
        return self.name


class Meta:
    verbose_name = 'Категория'
    verbose_name_plural = 'Категории'
