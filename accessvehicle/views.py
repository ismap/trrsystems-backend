import os
import datetime

from django.http import HttpResponse

from django.template.loader import render_to_string
from weasyprint import HTML
#os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")

from django.views.generic.base import TemplateView
from django.views.generic.dates import YearArchiveView

from .models import AccessVehicle

from rest_framework import viewsets
from .serializers import AccessControlSerializer

# Create your views here.

#class DashboardView(TemplateView):
    #template_name = 'dashboard.html'

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #context['today_access'] = AccessVehicle.objects.all().order_by('-access_date').filter(access_date__date=datetime.date.today())
        #return context

#class AccessYearArchiveView(YearArchiveView):
    #template_name = 'access_year_archive.html'
    #queryset = AccessVehicle.objects.all()
    #paginate_by = 10
    #make_object_list = True
    #date_field = 'access_date'
    #allow_future = True

class AccessControlViewSet(viewsets.ModelViewSet):
    queryset = AccessVehicle.objects.all()
    queryset= AccessVehicle.objects.all().order_by('-access_date').filter(access_date__date=datetime.date.today())
    serializer_class = AccessControlSerializer
    filterset_fields = ['access_inspection_completed']

#def PortableDocumentFormatView(request, id):
    #context =  {'a': AccessVehicle.objects.get(pk=id)}
    #html = render_to_string('report.html', context)

    #response = HttpResponse(content_type="application/pdf")
    #response["Content-Disposition"] = "inline; report.pdf"

    #HTML(string=html).write_pdf(response)
    #return response