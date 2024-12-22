from django.shortcuts import render
from .serializers import Serializer
from .models import Announcement
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


# Create your views here.


class AnnouncementCreateAPIView(generics.ListCreateAPIView):
    queryset = Announcement.objects.filter(is_deleted=False)
    serializer_class = Serializer

    def get(self, request, *args, **kwargs):
        records = self.get_queryset()
        serializer = Serializer(records, many=True)
        return Response(serializer.data)
    
class AnnouncementUpdateAPIView(APIView):

    def get_object(self, pk):
        """Helper method to get the object by ID, handling soft deletes."""
        return get_object_or_404(Announcement, pk=pk, is_deleted=False)
    
    def put(self, request, pk, *args, **kwargs):
        """Update a specific ConsultantExperience by ID."""
        records = self.get_object(pk)
        serializer = Serializer(records, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class Getbyid(RetrieveAPIView):
    queryset = Announcement.objects.filter(is_deleted=False)
    serializer_class = Serializer

    def get_object(self):
        try:
            return super().get_object()
        except Announcement.DoesNotExist:
            raise NotFound({"error": "Record not found"})
        
class Delete(APIView):
    def delete(self, request, pk):
        try:
            record = Announcement.objects.get(pk=pk, is_deleted=False)
        except Announcement.DoesNotExist:
            return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)

        record.is_deleted = True
        record.save()
        return Response({"message": "Record deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
class FilterByModuleandType(APIView):
    def get(self, request, module, type):
        records = Announcement.objects.filter(module=module, type=type, is_deleted=False)
        serializer = Serializer(records, many=True)
        return Response(serializer.data)