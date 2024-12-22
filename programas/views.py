from rest_framework import filters
from backend_mmaya.views import SoftDeleteModelViewSet
from .models import *
from .serializers import  ProgramasSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ProgramaSerializerViewSet(SoftDeleteModelViewSet):
    queryset = Programas.objects.all().prefetch_related('sectorprograma_set__sector','sectorprograma_set','proyectos_set')
    serializer_class = ProgramasSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['viceministerio','sigla_prog_convenio','programas_proyectos']
    ordering_fields = ['sigla_prog_convenio']
    ordering = ['sigla_prog_convenio']
