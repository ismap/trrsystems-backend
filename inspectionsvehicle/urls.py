from django.urls import include, path
from .views import InspectionViewSet

from .views import ArchiveView, generate_pdf

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'', InspectionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    
    path('archivo/', ArchiveView.as_view(), name="archive_inspections"),
    path('report/<int:id>/', generate_pdf, name='pdf' )
]
