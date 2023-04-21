from django.urls import include, path
from .views import InspectionViewSet

from .views import ArchiveView, ArchiveYearView, ArchiveMonthView, ArchiveTodayView, generate_pdf

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'', InspectionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    
    path('archivo/', ArchiveView.as_view(), name="archive_inspections"),
    path('archivo/<int:year>/', ArchiveYearView.as_view(), name="archive_inspections_year"),
    path('archivo/<int:year>/<int:month>/', ArchiveMonthView.as_view(month_format="%m"), name="archive_inspections_month"),
    path('archivo/hoy/', ArchiveTodayView.as_view(), name="archive_today_inspections"),
    path('report/<int:id>/', generate_pdf, name='pdf' )
]
