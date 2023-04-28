from contextlib import nullcontext
from distutils.command import upload
from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_create = models.DateTimeField(auto_now_add=True)
    employee_name = models.CharField(max_length=50)
    employee_number = models.CharField(max_length=50, primary_key=True)
    employee_rfc = models.CharField(max_length=50)
    employee_photo = models.ImageField(upload_to='Empleados/Oficinas', null=True)
    employee_signature = models.ImageField(upload_to='Empleados/Oficinas', null=True)

class EmployeeTruck(models.Model):
    employee_create = models.DateTimeField(auto_now_add=True)
    employee_name = models.CharField(max_length=50)
    employee_number = models.CharField(max_length=50, primary_key=True)
    employee_license = models.CharField(max_length=50)
    employee_rfc = models.CharField(max_length=50)
    employee_photo = models.ImageField(upload_to='Empleados/Operadores', blank=True, null=True)
    employee_signature = models.ImageField(upload_to='Empleados/Operadores', blank=True, null=True)