from django.contrib.auth.models import User
from django.db import models

from .requirement import Requirement


class RequirementPermission(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    requirement = models.ForeignKey(Requirement, models.CASCADE)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'procedure_resource_requirement_permission'
        unique_together = (('user', 'requirement'))

    def __str__(self):
        return self.user.username + ' ' + self.requirement.name
