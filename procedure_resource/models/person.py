from django.contrib.auth.models import User
from django.db import models
import datetime

from .procedure import Procedure


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

    procedures = models.ManyToManyField(Procedure, through='PersonProcedure', verbose_name='trámites')

    class Meta:
        verbose_name = 'persona'

    def __str__(self):
        return self.name


class PersonProcedure(models.Model):
    STATUS_PENDING = 1  # Pendiente
    STATUS_INIT = 2  # Inicializado
    STATUS_CANCEL = 3  # Cancelado
    STATUS_FINISHED = 4  # Terminado
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pendiente'),
        (STATUS_INIT, 'Inicializado'),
        (STATUS_CANCEL, 'Cancelado'),
        (STATUS_FINISHED, 'Terminado'),
    ]

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
    )
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name
