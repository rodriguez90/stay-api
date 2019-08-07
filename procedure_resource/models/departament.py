from django.db import models


class Departament(models.Model):
    name = models.CharField(max_length=255, verbose_name='nombre')
    description = models.TextField(blank=True, verbose_name='descripción')
    is_active = models.BooleanField(default=True, verbose_name='esta activo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
