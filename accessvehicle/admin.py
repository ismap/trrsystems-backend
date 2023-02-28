from django.contrib import admin
from .models import AccessVehicle

# Register your models here.

class AccessVehicleAdmin(admin.ModelAdmin):
    pass
admin.site.register(AccessVehicle, AccessVehicleAdmin)
