from django.contrib import admin
from .models import Employee, EmployeeTruck

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Employee, EmployeeAdmin)

class EmployeeTruckAdmin(admin.ModelAdmin):
    pass
admin.site.register(EmployeeTruck, EmployeeTruckAdmin)