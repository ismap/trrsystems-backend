from dataclasses import field
from .models import Employee, EmployeeTruck
from rest_framework import serializers

class CatalogEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class CatalogEmployeeTruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTruck
        fields = '__all__'