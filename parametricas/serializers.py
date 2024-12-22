from rest_framework import serializers
from .models import *
from backend_mmaya.serializers import BaseCrudSerializer

class ParametricaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parametrica
        fields = ['id', 'nombre', 'valor', 'codigo', 'tabla', 'estado','is_deleted']
