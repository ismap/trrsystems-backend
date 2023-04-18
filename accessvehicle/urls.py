from django.urls import path, include

from .views import AccessControlViewSet

from .views import ArchiveView, ArchiveYearView, ArchiveMonthView, ArchiveWeekView, ArchiveTodayView

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', AccessControlViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

    path('archivo/', ArchiveView.as_view(), name="archive"),
    path('archivo/<int:year>/', ArchiveYearView.as_view(), name="archive_year"),
    path('archivo/<int:year>/<int:month>/', ArchiveMonthView.as_view(month_format="%m"), name="archive_month"),
    path("<int:year>/week/<int:week>/", ArchiveWeekView.as_view(), name="archive_week",),
    path('archivo/hoy/', ArchiveTodayView.as_view(), name="archive_today"),
]
