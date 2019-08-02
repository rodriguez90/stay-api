from django.contrib.auth.models import User
from django.db import models


class UserProcedure(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    procedure = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
