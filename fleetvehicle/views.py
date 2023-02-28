from .models import Truck, Trailer

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CatalogTruckSerializer, CatalogTrailerSerializer

# Create your views here.

class CatalogTruckViewSet(viewsets.ModelViewSet):
    queryset = Truck.objects.all()
    serializer_class = CatalogTruckSerializer
    def get_queryset(self):
        queryset = Truck.objects.all()
        truckcode = self.request.query_params.get('truck_code')
        trucknumber = self.request.query_params.get('truck_number')
        if truckcode is not None:
            queryset = queryset.filter(truck_code=truckcode)
            return queryset
        if trucknumber is not None:
            queryset = queryset.filter(truck_number=trucknumber)
            return queryset

class CatalogTrailerViewSet(viewsets.ModelViewSet):
    queryset = Trailer.objects.all()
    serializer_class = CatalogTrailerSerializer
    #filterset_fields = ['trailer_code','trailer_number']
    def get_queryset(self):
        queryset = Trailer.objects.all()
        trailercode = self.request.query_params.get('trailer_code')
        trailernumber = self.request.query_params.get('trailer_number')
        if trailercode is not None:
            queryset = queryset.filter(trailer_code=trailercode)
            return queryset
        if trailernumber is not None:
            queryset = queryset.filter(trailer_number=trailernumber)
            return queryset