from django.urls import path, include
from rest_framework import routers

from .views import CatalogEmployeeViewSet, CatalogEmployeeTruckViewSet

router = routers.DefaultRouter()
router.register(r'administrativos', CatalogEmployeeViewSet)
router.register(r'operativos', CatalogEmployeeTruckViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
