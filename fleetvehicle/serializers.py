from dataclasses import fields
from pyexpat import model
from .models import Truck, Trailer
from employees.models import EmployeeTruck

from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTruck
        fields = ['employee_number','employee_name','employee_license','employee_rfc','employee_photo','employee_signature']

class CatalogTruckSerializer(serializers.ModelSerializer):
    truck_driver = EmployeeSerializer()
    class Meta:
        model = Truck
        fields = ['truck_number','truck_code','truck_model','truck_plates', 'truck_serial', 'truck_engine', 'truck_driver']

class CatalogTrailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trailer
        fields = ['trailer_number', 'trailer_code' ,'trailer_plate', 'trailer_model', 'trailer_serial', 'trailer_type']