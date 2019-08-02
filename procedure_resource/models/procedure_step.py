from django.db import models

from .departament import Departament
from .procedure import Procedure
from .document_type import DocumentType


class ProcedureStep(models.Model):
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE)
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    requirements = models.ManyToManyField(DocumentType)

    name = models.CharField(max_length=255)
    description = models.TextField()
    position = models.SmallIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
