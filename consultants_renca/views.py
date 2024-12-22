from rest_framework import generics, permissions, status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import ConsultantRenca, DepositRenca, ConsultantExperienceRenca
from .serializers import ConsultantRencaSerializer, ConsultantExperienceRencaSerializer, ConsultantRencaSerializer, ConsultantExperienceRencaBulkCreateSerializer, DepositRencaSerializer, BulkCreateDepositRencaSerializer
from parameters.serializers import BankAccountSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

class ConsultantRencaListCreateAPIView(generics.ListCreateAPIView):
    queryset = ConsultantRenca.objects.filter(is_deleted=False)
    serializer_class = ConsultantRencaSerializer
    #permission_classes = [permissions.IsAuthenticated]

class ConsultantRencaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConsultantRenca.objects.filter(is_deleted=False)
    serializer_class = ConsultantRencaSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

class BulkCreateDepositRencaView(APIView):
    def post(self, request):
        serializer = BulkCreateDepositRencaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Deposits created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditDepositRencaView(APIView):
    def put(self, request, pk):
        try:
            deposit = DepositRenca.objects.get(pk=pk, is_deleted=False)
        except DepositRenca.DoesNotExist:
            return Response({"error": "Deposit not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = DepositRencaSerializer(deposit, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Deposit updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteDepositRencaView(APIView):
    def delete(self, request, pk):
        try:
            deposit = DepositRenca.objects.get(pk=pk, is_deleted=False)
        except DepositRenca.DoesNotExist:
            return Response({"error": "Deposit not found"}, status=status.HTTP_404_NOT_FOUND)

        deposit.is_deleted = True
        deposit.save()
        return Response({"message": "Deposit deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class ListDepositsRencaView(ListAPIView):
    queryset = DepositRenca.objects.filter(is_deleted=False)
    serializer_class = DepositRencaSerializer

class RetrieveDepositRencaView(RetrieveAPIView):
    queryset = DepositRenca.objects.filter(is_deleted=False)
    serializer_class = DepositRencaSerializer

    def get_object(self):
        try:
            return super().get_object()
        except DepositRenca.DoesNotExist:
            raise NotFound({"error": "Deposit not found"})

class ConsultantExperienceRencaListCreateAPIView(generics.GenericAPIView):
    queryset = ConsultantExperienceRenca.objects.filter(is_deleted=False)
    serializer_class = ConsultantExperienceRencaBulkCreateSerializer

    def get(self, request, *args, **kwargs):
        experiences = self.get_queryset()
        serializer = ConsultantExperienceRencaSerializer(experiences, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # Obtener el JSON del campo "experiences"
        experiences_data = request.data.get('experiences')
        if not experiences_data:
            return Response({"error": "El campo 'experiences' es requerido."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            experiences_data = json.loads(experiences_data)  # Convertir el JSON a una lista Python
        except json.JSONDecodeError:
            return Response({"error": "El campo 'experiences' no contiene un JSON válido."}, status=status.HTTP_400_BAD_REQUEST)

        if not isinstance(experiences_data, list):
            return Response({"error": "El campo 'experiences' debe ser una lista."}, status=status.HTTP_400_BAD_REQUEST)

        experiences = []
        for idx, experience_data in enumerate(experiences_data):
            # Asociar archivo al índice correspondiente
            file_key = f"files[{idx}]"
            certificate_file = request.FILES.get(file_key)
            if certificate_file:
                experience_data['certificate_file'] = certificate_file

            # Crear la experiencia
            serializer = ConsultantExperienceRencaSerializer(data=experience_data)
            serializer.is_valid(raise_exception=True)
            experience = serializer.save()
            experiences.append(experience)

        response_serializer = ConsultantExperienceRencaSerializer(experiences, many=True)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    
class ConsultantExperienceRencaDetailAPIView(APIView):
    def get_object(self, pk):
        """Helper method to get the object by ID, handling soft deletes."""
        return get_object_or_404(ConsultantExperienceRenca, pk=pk, is_deleted=False)

    def get(self, request, pk, *args, **kwargs):
        """Retrieve a specific ConsultantExperience by ID."""
        experience = self.get_object(pk)
        serializer = ConsultantExperienceRencaSerializer(experience)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        """Update a specific ConsultantExperience by ID."""
        experience = self.get_object(pk)
        serializer = ConsultantExperienceRencaSerializer(experience, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, *args, **kwargs):
        """Soft delete a specific ConsultantExperience by ID."""
        experience = self.get_object(pk)
        experience.is_deleted = True
        experience.save()
        return Response({"detail": "Experience deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

class ConsultantExperienceRencaRetrieveAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        """Retrieve a specific ConsultantExperience by ID."""
        experience = get_object_or_404(ConsultantExperienceRenca, pk=pk, is_deleted=False)
        serializer = ConsultantExperienceRencaSerializer(experience)
        return Response(serializer.data)


