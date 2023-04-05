from django.urls import path, include

from .views import AccessControlViewSet

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'', AccessControlViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    #path('', DashboardView.as_view(), name='accessDashboard'),
    #path('archivo/year/<int:year>', AccessYearArchiveView.as_view(), name='archive_year'),
    #path('report/<int:id>/', PortableDocumentFormatView, name='pdf' )
]
