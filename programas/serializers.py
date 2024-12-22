from rest_framework import serializers
from parametros.models import SectorPrograma
from .models import Programas

class ProgramasSerializer(serializers.ModelSerializer):
    sector_ids = serializers.ListField(child=serializers.IntegerField(), write_only=True, required=False)
    sectores = serializers.SerializerMethodField()  # Campo adicional para los sectores
    numero_proyectos = serializers.IntegerField(
        source='proyectos_set.count', 
        read_only=True
    )

    class Meta:
        model = Programas
        fields = '__all__'
  
