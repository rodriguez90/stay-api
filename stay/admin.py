from django.contrib import admin

# Register your models here.

from stay.models import *

admin.site.register(Person)
admin.site.register(Rent)
admin.site.register(Service)
