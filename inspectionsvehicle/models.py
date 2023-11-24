from contextlib import nullcontext
from pickle import TRUE
from django.db import models

from employees.models import Employee, EmployeeTruck
from fleetvehicle.models import Truck, Trailer

# Create your models here.

class Inspection(models.Model):

    CARRIER_CHOICES = [
        ('Transportes Refrigerados Rivas', 'Transportes Refrigerados Rivas')
    ]

    INSPECTION_CHOICES = [
        ('Con anomalías', 'Con anomalías'),
        ('Sin anomalías', 'Sin anomalías'),
    ]

    LOAD_CHOICES = [
        ('Con carga', 'Con carga'),
        ('Sin carga', 'Sin carga'),
    ]

    INSPECTION_DOCUMENT_CHOICES = [
        ('Sí', 'Sí'),
        ('No', 'No'),
    ]

    inspection_create = models.DateTimeField(auto_now=True)
    inspection_carrier = models.CharField(max_length=100, choices=CARRIER_CHOICES, null=True)
    inspection_inspector = models.ForeignKey(Employee, on_delete=models.PROTECT, null=True)

    inspection_truck_number = models.ForeignKey(Truck, on_delete=models.CASCADE, null=True)
    inspection_truck_defense = models.CharField(max_length=100, choices=INSPECTION_CHOICES, null=True)
    inspection_truck_defense_image = models.ImageField(upload_to='Inspecciones/Tractocamiones', null=True, blank=True)
    inspection_truck_engine = models.CharField(max_length=100, choices=INSPECTION_CHOICES, null=True)
    inspection_truck_engine_image = models.ImageField(upload_to='Inspecciones/Tractocamiones', null=True, blank=True)
    inspection_truck_tires = models.CharField(max_length=100, choices=INSPECTION_CHOICES, null=True)
    inspection_truck_tires_image = models.ImageField(upload_to='Inspecciones/Tractocamiones', null=True, blank=True)
    inspection_truck_fueltank = models.CharField(max_length=100, choices=INSPECTION_CHOICES, null=True)
    inspection_truck_fueltank_image = models.ImageField(upload_to='Inspecciones/Tractocamiones', null=True, blank=True)
    

    inspection_box_number = models.ForeignKey(Trailer, on_delete=models.PROTECT, null=True)
    inspection_box_coolingunit = models.CharField(max_length=100, choices=INSPECTION_CHOICES, null=True)
    inspection_box_coolingunit_image = models.ImageField(upload_to='Inspecciones/Cajas', null=True, blank=True)
    inspection_box_leftwall = models.CharField(max_length=100, choices=INSPECTION_CHOICES, null=True)
    inspection_box_leftwall_image = models.ImageField(upload_to='Inspecciones/Cajas', null=True, blank=True)
    inspection_box_rightwall = models.CharField(max_length=100, choices=INSPECTION_CHOICES, null=True)
    inspection_box_rightwall_image = models.ImageField(upload_to='Inspecciones/Cajas', null=True, blank=True)
    inspection_box_backdoors = models.CharField(max_length=100, choices=INSPECTION_CHOICES, null=True)
    inspection_box_backdoors_image = models.ImageField(upload_to='Inspecciones/Cajas', null=True, blank=True)

    inspection_box_load = models.CharField(max_length=100, choices=LOAD_CHOICES, null=True)
    inspection_box_backdoors_inside = models.CharField(max_length=100, choices=INSPECTION_CHOICES, null=True)
    inspection_box_backdoors_inside_image = models.ImageField(upload_to='Inspecciones/Cajas', null=True, blank=True)
    inspection_box_airduct = models.CharField(max_length=100, choices=INSPECTION_CHOICES, null=True)
    inspection_box_walls_inside = models.CharField(max_length=100, choices=INSPECTION_CHOICES, null=True)
    inspection_box_walls_inside_image = models.ImageField(upload_to='Inspecciones/Cajas', null=True, blank=True)
    inspection_box_floor = models.CharField(max_length=100, choices=INSPECTION_CHOICES, null=True)

    inspection_box_under = models.CharField(max_length=100, choices=INSPECTION_CHOICES, null=True)
    inspection_box_under_image = models.ImageField(upload_to='Inspecciones/Cajas', null=True, blank=True)
    inspection_box_tires = models.CharField(max_length=100, choices=INSPECTION_CHOICES, null=True)
    inspection_box_tires_image = models.ImageField(upload_to='Inspecciones/Cajas', null=True, blank=True)
    inspection_box_seal = models.CharField(max_length=100, null=True)
    inspection_box_seal_image = models.ImageField(upload_to='Inspecciones/Cajas', null=True, blank=True)
    inspection_box_pollutants = models.CharField(max_length=100, choices=INSPECTION_CHOICES, null=True)
    inspection_box_pollutants_image = models.ImageField(upload_to='Inspecciones/Cajas', null=True, blank=True)

    inspection_document_cp = models.CharField(max_length=100, choices=INSPECTION_DOCUMENT_CHOICES, null=True, blank=True)
    inspection_document_cp_number = models.CharField(max_length=100, null=True, blank=True)

    inspection_document_departamentmotors = models.CharField(max_length=100, choices=INSPECTION_DOCUMENT_CHOICES, null=True)
    inspection_document_invoice = models.CharField(max_length=100, choices=INSPECTION_DOCUMENT_CHOICES, null=True)
    inspection_document_circulation = models.CharField(max_length=100, choices=INSPECTION_DOCUMENT_CHOICES, null=True)
    inspection_document_physicalmechanics =  models.CharField(max_length=100, choices=INSPECTION_DOCUMENT_CHOICES, null=True)
    inspection_document_securepolicy = models.CharField(max_length=100, choices=INSPECTION_DOCUMENT_CHOICES, null=True)
    
    inspection_signature_driver = models.ImageField(upload_to='Inpecciones/Firmas', null=True, blank=True)

    def __str__(self):
        return str(self.id)
    
