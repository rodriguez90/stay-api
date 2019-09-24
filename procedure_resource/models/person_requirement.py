from django.db import models
from .person import PersonProcedure
from .requirement import Requirement
from .document import Document


class PersonRequirement(models.Model):
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

    person_procedure = models.ForeignKey(PersonProcedure, on_delete=models.CASCADE)
    procedure_step = models.ForeignKey(Requirement, on_delete=models.CASCADE)
    requirements = models.ManyToManyField(Document, through='PersonRequirementDocument')
    id = models.AutoField(primary_key=True)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
    )
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PersonRequirementDocument(models.Model):
    STATUS_PENDING = 1  # Pendiente
    STATUS_CANCEL = 3  # Rechazado
    STATUS_FINISHED = 4  # Aceptado
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pendiente'),
        (STATUS_CANCEL, 'Rechazado'),
        (STATUS_FINISHED, 'Aceptado'),
    ]

    id = models.AutoField(primary_key=True)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    person_procedure_step = models.ForeignKey(PersonRequirement, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
    )
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
