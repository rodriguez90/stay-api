from django.contrib import admin

# Register your models here.

from procedure_resource.models import *

admin.site.register(Departament)
admin.site.register(DocumentType)
admin.site.register(Procedure)
admin.site.register(ProcedureStep)
