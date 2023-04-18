from django.template.loader import get_template
from xhtml2pdf import pisa


from django.http import HttpResponse

from django.views.generic.dates import ArchiveIndexView
from django.views.generic.dates import YearArchiveView
from django.views.generic.dates import MonthArchiveView
from django.views.generic.dates import TodayArchiveView

from .models import Inspection
from accessvehicle.models import AccessVehicle

from rest_framework import viewsets
from .serializers import AccessControlSerializer, InspectionSerializer

# Create your views here.

class InspectionViewSet(viewsets.ModelViewSet):
    queryset= AccessVehicle.objects.all().order_by('-access_date')
    serializer_class = AccessControlSerializer
    
class ArchiveView(ArchiveIndexView):
    template_name= 'archive_inspections_view.html'
    queryset = AccessVehicle.objects.all()
    date_field= 'access_date'
    paginate_by = 10

def generate_pdf(request, id):
    # Obtener la plantilla HTML
    template = get_template('report.html')
    context =  {'a': AccessVehicle.objects.get(pk=id)}
    html = template.render(context)
    
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="archivo.pdf"'
    
    pisaStatus = pisa.CreatePDF(html, dest=response)
    if pisaStatus.err:
        return HttpResponse('Error al generar el PDF: %s' % pisaStatus.err, status=500)

    return response





