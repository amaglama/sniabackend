from django.shortcuts import render
from .serializers import SerializerAnnouncement, SerializerAnnouncementModule, SerializerAnnouncementType
from .models import Announcement, AnnouncementType, AnnouncementModule
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
from django.db.models import OuterRef, Subquery, Value, CharField, BigIntegerField
from django.db.models.functions import Cast


# Create your views here.


class AnnouncementCreateAPIView(generics.ListCreateAPIView):
    queryset = Announcement.objects.filter(is_deleted=False).annotate(
    module_name=Subquery(
        AnnouncementModule.objects.filter(
            id=Cast(OuterRef('id_module'), output_field=BigIntegerField())
        ).values('name')[:1]
    ),
    type_name=Subquery(
        AnnouncementType.objects.filter(
            id=Cast(OuterRef('id_type'), output_field=BigIntegerField())
        ).values('name')[:1]
    )
)
    serializer_class = SerializerAnnouncement
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        filename = request.data.get('file')
        request.data['filename'] = filename.name
        serializer = SerializerAnnouncement(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def get(self, request, *args, **kwargs):
        records = self.get_queryset().order_by('-created_at')
        serializer = SerializerAnnouncement(records, many=True)
        return Response(serializer.data)
    
class AnnouncementUpdateAPIView(APIView):

    def get_object(self, pk):
        """Helper method to get the object by ID, handling soft deletes."""
        return get_object_or_404(Announcement, pk=pk, is_deleted=False)
    
    def put(self, request, pk, *args, **kwargs):
        """Update a specific ConsultantExperience by ID."""
        records = self.get_object(pk)
        serializer = SerializerAnnouncement(records, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class Getbyid(RetrieveAPIView):
    queryset = Announcement.objects.filter(is_deleted=False)
    serializer_class = SerializerAnnouncement

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
    def get(self, request, id_module, id_type):
        records = Announcement.objects.filter(id_module=id_module, id_type=id_type, is_deleted=False).order_by('-created_at')
        serializer = SerializerAnnouncement(records, many=True)
        return Response(serializer.data)
    
class ModuleList(APIView):
    def get(self, request, *args, **kwargs):
        records = AnnouncementModule.objects.filter(is_deleted=False).order_by('-created_at')
        serializer = SerializerAnnouncementModule(records, many=True)
        return Response(serializer.data)
    

class TypeList(APIView):
    def get(self, request, *args, **kwargs):
        records = AnnouncementType.objects.filter(is_deleted=False).order_by('-created_at')
        serializer = SerializerAnnouncementType(records, many=True)
        return Response(serializer.data)