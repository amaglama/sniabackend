from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics, permissions, status
from rest_framework.generics import ListAPIView, RetrieveAPIView

from rest_framework.views import APIView


from .serializers import RentraaSerializer
from .models import Rentraa

from rest_framework.response import Response


from rest_framework.exceptions import NotFound



# Create your views here.
def hello_world(request):
    return HttpResponse("Hello, World!")

class RegistroCreateAPIView(generics.ListCreateAPIView):
    queryset = Rentraa.objects.filter(is_deleted=False)
    serializer_class = RentraaSerializer

    def get(self, request, *args, **kwargs):
        records = self.get_queryset()
        serializer = RentraaSerializer(records, many=True)
        return Response(serializer.data)
    

class RetrieveRecord(RetrieveAPIView):
    queryset = Rentraa.objects.filter(is_deleted=False)
    serializer_class = RentraaSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Rentraa.DoesNotExist:
            raise NotFound({"error": "Deposit not found"})


class DeleteRecord(APIView):
    def delete(self, request, pk):
        try:
            record = Rentraa.objects.get(pk=pk, is_deleted=False)
        except Rentraa.DoesNotExist:
            return Response({"error": "Deposit not found"}, status=status.HTTP_404_NOT_FOUND)

        record.is_deleted = True
        record.save()
        return Response({"message": "Deposit deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

