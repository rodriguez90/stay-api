from django.db import models
from django.contrib.auth.models import User

from .service import Service


class Rent(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')
    description = models.TextField(verbose_name='description')
    is_active = models.BooleanField(default=True, verbose_name='status')
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    price = models.FloatField(blank=False, null=False, verbose_name='price')
    phone = models.CharField(max_length=255, verbose_name='phone', blank=False, null=False)
    email = models.EmailField(max_length=255, verbose_name='email', blank=False, null=False)
    adress = models.CharField(max_length=255, verbose_name='adress', blank=False, null=False)
    image = models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='imagen')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    services = models.ManyToManyField(Service,
                                         through='RentService',
                                         through_fields=('rent', 'service'),
                                         verbose_name='services',
                                         related_name='services')

    def __str__(self):
        return self.name


class RentService(models.Model):
    rent = models.ForeignKey(Rent, models.CASCADE)
    service = models.ForeignKey(Service, models.CASCADE)


class RentImages(models.Model):
    image = models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='imagen')
    rent = models.ForeignKey(Rent, models.CASCADE, related_name='images')

