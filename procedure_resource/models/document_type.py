from django.db import models


class DocumentType(models.Model):
    name = models.CharField(max_length=255, verbose_name='nombre')
    description = models.TextField(blank=True, null=True, verbose_name='descripción')
    is_active = models.BooleanField(default=True, verbose_name='esta activo')
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, null=True, verbose_name='Enlace de descarga')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
