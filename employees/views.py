from .models import Employee, EmployeeTruck
from .serializers import CatalogEmployeeSerializer, CatalogEmployeeTruckSerializer

from rest_framework import viewsets

# Create your views here.

class CatalogEmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = CatalogEmployeeSerializer
    filterset_fields = ['employee_number']

class CatalogEmployeeTruckViewSet(viewsets.ModelViewSet):
    queryset = EmployeeTruck.objects.all()
    serializer_class = CatalogEmployeeTruckSerializer
    filterset_fields = ['employee_number','employee_license']