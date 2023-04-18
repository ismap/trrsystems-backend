

from django.views.generic.dates import ArchiveIndexView
from django.views.generic.dates import YearArchiveView
from django.views.generic.dates import MonthArchiveView
from django.views.generic.dates import WeekArchiveView
from django.views.generic.dates import TodayArchiveView

from .models import AccessVehicle

from rest_framework import viewsets
from .serializers import AccessControlSerializer

from openpyxl import Workbook
from django.http import HttpResponse

# Create your views here.
class ArchiveView(ArchiveIndexView):
    template_name= 'archive_view.html'
    queryset = AccessVehicle.objects.all()
    date_field= 'access_date'
    paginate_by = 10

class ArchiveYearView(YearArchiveView):
    template_name= 'archive_year_view.html'
    queryset = AccessVehicle.objects.all()
    date_field= 'access_date'
    make_object_list= True
    allow_future= True
    paginate_by = 10
    
class ArchiveMonthView(MonthArchiveView):
    template_name= 'archive_month_view.html'
    queryset = AccessVehicle.objects.all()
    date_field= "access_date"
    allow_future= True
    paginate_by = 10
    
class ArchiveWeekView(WeekArchiveView):
    template_name= 'archive_week_view.html'
    queryset = AccessVehicle.objects.all()
    date_field = "access_date"
    week_format = "%W"
    allow_future = True

class ArchiveTodayView(TodayArchiveView):
    template_name= 'archive_today_view.html'
    queryset = AccessVehicle.objects.all()
    date_field = 'access_date'
    allow_future= True
    paginate_by = 10

class AccessControlViewSet(viewsets.ModelViewSet):
    queryset= AccessVehicle.objects.all().order_by('-access_date')
    #queryset= AccessVehicle.objects.all().order_by('-access_date').filter(access_date__date=datetime.date.today())
    serializer_class = AccessControlSerializer