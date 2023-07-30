from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Profile(models.Model):
    name = models.ForeignKey(User, on_delete=models.PROTECT)
    phone = models.CharField(max_length=20, verbose_name='telefon nomeri')
    email = models.EmailField(max_length=400, verbose_name='Elektron pochta')
    INN = models.CharField(max_length=20, verbose_name='INN')
    def __str__(self):
        return self.name


class Daraja(models.Model):
    turi = models.CharField(max_length=2, verbose_name='turi')
    nomi = models.CharField(max_length=500, verbose_name='Nomi')
    def __str__(self):
        return self.nomi

class Company(models.Model):
    name = models.CharField(max_length=255, verbose_name='Company name')
    turi = models.ForeignKey(Daraja, on_delete=models.CASCADE)
    rating = models.IntegerField(verbose_name='rating')
    inn = models.CharField(max_length=100, verbose_name='INN')
    izoh = models.TextField(verbose_name='Izoh')
    publish = models.BooleanField(default=False)
    def __str__(self):
        return self.name


