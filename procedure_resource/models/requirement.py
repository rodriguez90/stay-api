from django.db import models
from django.contrib.auth.models import User

from .departament import Departament
from .procedure import Procedure
from .document_type import DocumentType


class Requirement(models.Model):
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE, verbose_name='departamento')
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE, verbose_name='trámite', related_name='requirements')
    documents = models.ManyToManyField(DocumentType, verbose_name='documentos')
    permissions = models.ManyToManyField(User,
                                        through='RequirementPermission',
                                        through_fields=('requirement', 'user'),
                                        verbose_name='permissions',
                                        related_name='permissions')

    name = models.CharField(max_length=255, verbose_name='nombre')
    description = models.TextField(blank=True, verbose_name='descripción')
    position = models.PositiveIntegerField(verbose_name='orden')
    is_active = models.BooleanField(default=True, verbose_name='esta activo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
