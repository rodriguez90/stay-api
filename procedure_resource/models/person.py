from django.contrib.auth.models import User
from django.db import models
import datetime

from .procedure import Procedure


class Person(models.Model):
    user = models.OneToOneField(User, models.SET_NULL, null=True)

    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255)
    second_last_name = models.CharField(max_length=255, blank=True, null=True)
    identification = models.CharField(max_length=255, blank=True, null=True, unique=True)  # dni, ruc, pasaporte
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    procedures = models.ManyToManyField(Procedure, through='PersonProcedure')

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
