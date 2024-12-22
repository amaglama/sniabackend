from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from .models import Parametrica
from .serializers import ParametricaSerializer
from backend_mmaya.pagination import CustomPageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
#from django_filters import rest_framework as django_filters


class ParametricaViewSet(viewsets.ModelViewSet):
    serializer_class = ParametricaSerializer
    pagination_class = CustomPageNumberPagination  # Usar tu clase de paginación
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['tabla']
    ordering_fields = ['nombre', 'valor']
    ordering = ['nombre']  # Orden por defecto

    def get_queryset(self):
        # Obtener el parámetro 'parametrica' de la URL
        parametrica_value = self.request.query_params.get('parametrica', None)

        # Filtrar por estado "HABILITADO" y por el valor de 'parametrica' si está presente
        queryset = Parametrica.objects.not_deleted().filter(estado="HABILITADO")

        if parametrica_value:
            queryset = queryset.filter(tabla=parametrica_value)

        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
