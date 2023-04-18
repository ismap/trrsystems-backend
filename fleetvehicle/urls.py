from django.urls import include, path
from .views import CatalogTruckViewSet, CatalogTrailerViewSet

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'tractocamiones', CatalogTruckViewSet)
router.register(r'cajas', CatalogTrailerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
