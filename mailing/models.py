from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=100,verbose_name='ФИО',blank=False, null=False)
    email = models.EmailField(verbose_name='Почта')
    comment = models.CharField(max_length=200, verbose_name='Комментарий')


