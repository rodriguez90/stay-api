from django.db import models

from .departament import Departament
from .procedure import Procedure
from .document_type import DocumentType


class ProcedureStep(models.Model):
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE, verbose_name='departamento')
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE, verbose_name='trámite')
    requirements = models.ManyToManyField(DocumentType, verbose_name='requisitos')

    name = models.CharField(max_length=255, verbose_name='nombre')
    description = models.TextField(blank=True, verbose_name='descripción')
    position = models.SmallIntegerField(verbose_name='orden')
    is_active = models.BooleanField(default=True, verbose_name='esta activo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
