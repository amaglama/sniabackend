from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from programas.models import Realizaciones,Seguimiento
from .serializers import *
from decimal import Decimal

class bajaSeguimientoEspecificoAPIView(APIView):
    def put(self, request, *args,**kwargs):
        seguimiento_id = request.query_params.get('seguimiento_id')
        if seguimiento_id:
            try:
                seguimiento_instance=Seguimiento.objects.get(id=seguimiento_id)
                if seguimiento_instance and seguimiento_instance.is_deleted==True:
                        return Response({'message':'El registro ya se dio baja anteriormente'})
                ejecutado_financiero_mes=seguimiento_instance.avance_financiero_mes
                porcentaje_financiero_mes=seguimiento_instance.porcentaje_avance_financiero_mes
                porcentaje_fisico_mes=seguimiento_instance.porcentaje_avance_fisico_mes

                realizacion_instance = Realizaciones.objects.get(id=seguimiento_instance.realizacion_id)
            except:
                return Response({'message':'hubo un error al dar baja un seguimiento'},status=status.HTTP_400_BAD_REQUEST)

        realizacion_instance.avance_fisico = Decimal(realizacion_instance.avance_fisico)-porcentaje_fisico_mes
        realizacion_instance.avance_financiamiento = Decimal(realizacion_instance.avance_financiamiento)-porcentaje_financiero_mes
        realizacion_instance.saldo_presupuesto += ejecutado_financiero_mes
        realizacion_instance.eje_acum = Decimal(realizacion_instance.eje_acum)-ejecutado_financiero_mes
        realizacion_instance.save()
                
        # seguimiento_instance.is_deleted=True
        seguimiento_instance.save()

        return Response({'message':'Se dio baja correctamente al registro del seguimiento'},status=status.HTTP_200_OK)
def resetSeguimiento(seguimiento_id):
    if seguimiento_id:
            try:
                seguimiento_instance=Seguimiento.objects.get(id=seguimiento_id)
                if seguimiento_instance and seguimiento_instance.is_deleted==True:
                        return Response({'message':'El registro ya se dio baja anteriormente'})
                ejecutado_financiero_mes=seguimiento_instance.avance_financiero_mes
                porcentaje_financiero_mes=seguimiento_instance.porcentaje_avance_financiero_mes
                porcentaje_fisico_mes=seguimiento_instance.porcentaje_avance_fisico_mes

                realizacion_instance = Realizaciones.objects.get(id=seguimiento_instance.realizacion_id)
            except:
                return Response({'message':'hubo un error al dar baja un seguimiento'},status=status.HTTP_400_BAD_REQUEST)

            realizacion_instance.avance_fisico -= porcentaje_fisico_mes
            realizacion_instance.avance_financiamiento -= porcentaje_financiero_mes
            realizacion_instance.saldo_presupuesto += ejecutado_financiero_mes
            realizacion_instance.eje_acum -= ejecutado_financiero_mes
            realizacion_instance.save()
                
            # seguimiento_instance.is_deleted=True
            # seguimiento_instance.save()
            return True
    else:
        return False
