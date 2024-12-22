from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import State, BankAccount, Category, Province, Municipality
from .serializers import StateSerializer,BankAccountSerializer, CategorySerializer,  ProvinceSerializer, MunicipalitySerializer, MunicipalityReverseSerializer, StateCascadeSerializer, ProvinceCascadeSerializer, MunicipalityCascadeSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

class StateListCreateView(ListCreateAPIView):
    queryset = State.objects.filter(is_deleted=False)  # Excluir estados eliminados lógicamente
    serializer_class = StateSerializer
    
class StateRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = State.objects.filter(is_deleted=False).order_by('name') 
    serializer_class = StateSerializer

    def perform_destroy(self, instance):
        """
        En lugar de eliminar físicamente, marcamos el estado como eliminado lógicamente.
        """
        instance.is_deleted = True
        instance.save()

class ProvinceListCreateView(ListCreateAPIView):
    queryset = Province.objects.filter(is_deleted=False).order_by('province_name')
    serializer_class = ProvinceSerializer

class ProvinceRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Province.objects.filter(is_deleted=False).order_by('province_name')
    serializer_class = ProvinceSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

class MunicipalityListCreateView(ListCreateAPIView):
    queryset = Municipality.objects.filter(is_deleted=False).order_by('ulot_name')
    serializer_class = MunicipalitySerializer
class MunicipalityRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Municipality.objects.filter(is_deleted=False).order_by('ulot_name')
    serializer_class = MunicipalitySerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
class StateProvincesMunicipalitiesView(APIView):
    def get(self, request, state_id):
        try:
            # Obtener el estado especificado
            state = State.objects.get(id=state_id, is_deleted=False)
            
            # Obtener todas las provincias del estado
            provinces = Province.objects.filter(state=state, is_deleted=False)
            
            # Serializar las provincias y sus municipios
            response_data = []
            for province in provinces:
                municipalities = Municipality.objects.filter(province=province, is_deleted=False)
                response_data.append({
                    "province": ProvinceSerializer(province).data,
                    "municipalities": MunicipalitySerializer(municipalities, many=True).data
                })

            return Response({
                "state": {
                    "id": state.id,
                    "name": state.name,
                    "code": state.code
                },
                "provinces_with_municipalities": response_data
            }, status=200)

        except State.DoesNotExist:
            return Response({"detail": "State not found."}, status=404)


class MunicipalityReverseLookupView(RetrieveUpdateDestroyAPIView):
    queryset = Municipality.objects.filter(is_deleted=False)
    serializer_class = MunicipalityReverseSerializer
class BankAccountViewSet(ModelViewSet):
    queryset = BankAccount.objects.filter(is_deleted=False)
    serializer_class = BankAccountSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['representative_name', 'bank_name']  # Campos para filtrar
    ordering_fields = ['representative_name', 'bank_name']  # Campos para ordenar
    ordering = ['bank_name']  # Orden por defecto

    def destroy(self, request, *args, **kwargs):
        """Realiza un borrado lógico en lugar de eliminar físicamente."""
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)        
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.filter(is_deleted=False)
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'registration_fee', 'renewal_fee','abbreviation', 'type']  # Campos para filtrar
    ordering_fields = ['name', 'registration_fee', 'renewal_fee','abbreviation', 'type']  # Campos para ordenar
    ordering = ['id']  # Orden por defecto

    def destroy(self, request, *args, **kwargs):
        """Realiza un borrado lógico en lugar de eliminar físicamente."""
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#para los combos
class StateCascadeView(ListAPIView):
    queryset = State.objects.filter(is_deleted=False)
    serializer_class = StateCascadeSerializer


class ProvinceCascadeView(ListAPIView):
    serializer_class = ProvinceCascadeSerializer

    def get_queryset(self):
        state_id = self.kwargs.get('state_id')
        return Province.objects.filter(state_id=state_id, is_deleted=False).order_by('province_name')

class MunicipalityCascadeView(ListAPIView):
    serializer_class = MunicipalityCascadeSerializer

    def get_queryset(self):
        province_id = self.kwargs.get('province_id')
        return Municipality.objects.filter(province_id=province_id, is_deleted=False).order_by('ulot_name')
   