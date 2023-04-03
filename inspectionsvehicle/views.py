import os
##os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")
import datetime

from django.shortcuts import render
from django.http import HttpResponse

from django.template.loader import render_to_string
from weasyprint import HTML

from django.views.generic.base import TemplateView
from django.views.generic.dates import YearArchiveView
from django.views.generic.dates import MonthArchiveView

from .models import Inspection

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import InspectionSerializer

# Create your views here.

class InspectionViewSet(viewsets.ModelViewSet):
    queryset = Inspection.objects.all()
    #queryset= Inspection.objects.all().order_by('-inspection_create').filter(inspection_create__date=datetime.date.today())
    serializer_class = InspectionSerializer

class InspectionDashboardView(TemplateView):
    template_name = 'InspectionDashboardView.html'
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['today_inspections'] = Inspection.objects.all().order_by('-inspection_create').filter(inspection_create__date=datetime.date.today())
        context['latest_inspections'] = Inspection.objects.all().order_by('-inspection_create')[:5]

        return context

class InspectionYearArchiveView(YearArchiveView):
    template_name = 'InspectionYearArchiveView.html'
    queryset = Inspection.objects.all()
    paginate_by = 10
    date_field = "inspection_create"
    make_object_list = True
    allow_future = True

class InspectionMonthArchiveView(MonthArchiveView):
    template_name = 'InspectionMonthArchiveView.html'
    paginate_by = 10
    queryset = Inspection.objects.all()
    date_field = "inspection_create"
    allow_future = True

def InspectionReport(request, id):
    context =  {'i': Inspection.objects.get(pk=id)}
    html = render_to_string('InspectionReport.html', context)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "inline; report.pdf"

    HTML(string=html).write_pdf(response)
    return response
