from django.contrib import admin
from .models import Inspection

# Register your models here.

class InspectionsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Inspection, InspectionsAdmin)