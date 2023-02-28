from django.urls import include, path
from .views import InspectionDashboardView, InspectionYearArchiveView, InspectionMonthArchiveView, InspectionReport, InspectionViewSet

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'', InspectionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('dashboard/', InspectionDashboardView.as_view(), name='InspectionDashboard'),
    path('dashboard/report/<int:id>/', InspectionReport, name='InspectionReport'),

    path('dashboard/archive/year/<int:year>', InspectionYearArchiveView.as_view(), name="InspectionYearArchive"),
    path('dashboard/archive/year/<int:year>/<int:month>', InspectionMonthArchiveView.as_view(month_format="%m"), name="InspectionMonthArchive")
]
