from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name='nombre')
    css_icon = models.CharField(max_length=255, verbose_name='icono')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
