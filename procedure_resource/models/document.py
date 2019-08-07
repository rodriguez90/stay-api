from django.db import models
from .document_type import DocumentType


class Document(models.Model):
    name = models.CharField(max_length=255, verbose_name='nombre')
    md5 = models.BinaryField()
    content = models.BinaryField()
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
    type = models.ForeignKey(
        DocumentType,
        on_delete=models.PROTECT,
        verbose_name='Tipo'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
