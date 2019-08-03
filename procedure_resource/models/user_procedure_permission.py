from django.contrib.auth.models import User
from django.db import models

from .procedure import Procedure


class UserProcedurePermission(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    procedure = models.ForeignKey(Procedure, models.CASCADE)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
