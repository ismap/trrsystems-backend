from django.db import models

from inspectionsvehicle.models import Inspection
from fleetvehicle.models import Truck, Trailer

# Create your models here.

CONTROL_ACCESS_CHOICES = [
    ('Entrada de Unidad', 'Entrada de Unidad'),
    ('Salida de Unidad', 'Salida de Unidad')
]

class AccessVehicle(models.Model):
    access_date = models.DateTimeField(auto_now_add=True)
    access_control = models.CharField(max_length=50, choices=CONTROL_ACCESS_CHOICES)
    access_truck = models.ForeignKey(Truck, on_delete=models.PROTECT)
    access_trailer = models.ForeignKey(Trailer, on_delete=models.PROTECT)
    access_inspection = models.OneToOneField(Inspection, on_delete=models.CASCADE, blank=True , null=True)
    