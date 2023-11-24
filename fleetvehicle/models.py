from django.db import models
from employees.models import EmployeeTruck
# Create your models here.
class Truck(models.Model):
    truck_created = models.DateTimeField(auto_now_add=True)
    truck_modified = models.DateTimeField(auto_now=True)
    truck_code = models.CharField(max_length=50)
    truck_number = models.CharField(max_length=50, primary_key=True)
    truck_model = models.CharField(max_length=50)
    truck_plates = models.CharField(max_length=50)
    truck_serial = models.CharField(max_length=50)
    truck_engine = models.CharField(max_length=50)

    truck_driver = models.ForeignKey(EmployeeTruck, on_delete=models.PROTECT, blank=True , null=True)
    def __str__(self):
        return self.truck_number

class Trailer(models.Model):
    trailer_created = models.DateTimeField(auto_now_add=True)
    trailer_modified = models.DateTimeField(auto_now=True)
    trailer_code = models.CharField(max_length=50)
    trailer_number = models.CharField(max_length=50, primary_key=True)
    trailer_plate = models.CharField(max_length=50)
    trailer_model = models.CharField(max_length=50)
    trailer_serial = models.CharField(max_length=50)
    trailer_type = models.CharField(max_length=50)
    def __str__(self):
        return self.trailer_number  