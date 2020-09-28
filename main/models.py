from django.db import models

class User(models.Model):
    first_name = models.CharField('Имя', max_length = 50)
    last_name = models.CharField('Фамилия', max_length=50)

class Task(models.Model):
    title = models.CharField('Название', max_length = 50)
    text = models.TextField('Описание')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
