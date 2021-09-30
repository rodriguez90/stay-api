from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='usuario', on_delete=models.CASCADE)

    second_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='segundo nombre')
    second_last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='segundo apellido')
    identification = models.CharField(max_length=255, blank=True, null=True, unique=True, verbose_name='identificación')  # dni, ruc, pasaporte
    phone_number = models.CharField(max_length=255, blank=True, null=True, verbose_name='Teléfono')
    address = models.TextField(blank=True, null=True, verbose_name='dirección')

    is_active = models.BooleanField(default=True, verbose_name='esta activo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='actualizdo el')

    class Meta:
        verbose_name = 'persona'

    def __str__(self):
        return self.name
