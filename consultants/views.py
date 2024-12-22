from rest_framework import generics, status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Consultant, Deposit, ConsultantExperience
from .serializers import ConsultantSerializer, ConsultantExperienceSerializer, ConsultantExperienceBulkCreateSerializer, DepositSerializer, BulkCreateDepositSerializer
#from parameters.serializers import BankAccountSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from django.core.mail import send_mail
from .serializers import RegistrationSerializer
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .serializers import ConsultantValidationSerializer, ObservationSerializer
class ConsultantListCreateAPIView(generics.ListCreateAPIView):
    queryset = Consultant.objects.filter(is_deleted=False)
    serializer_class = ConsultantSerializer

class ConsultantRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consultant.objects.filter(is_deleted=False)
    serializer_class = ConsultantSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

class BulkCreateDepositView(APIView):
    def post(self, request):
        serializer = BulkCreateDepositSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Deposits created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditDepositView(APIView):
    def put(self, request, pk):
        try:
            deposit = Deposit.objects.get(pk=pk, is_deleted=False)
        except Deposit.DoesNotExist:
            return Response({"error": "Deposit not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = DepositSerializer(deposit, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Deposit updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteDepositView(APIView):
    def delete(self, request, pk):
        try:
            deposit = Deposit.objects.get(pk=pk, is_deleted=False)
        except Deposit.DoesNotExist:
            return Response({"error": "Deposit not found"}, status=status.HTTP_404_NOT_FOUND)

        deposit.is_deleted = True
        deposit.save()
        return Response({"message": "Deposit deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class ListDepositsView(ListAPIView):
    queryset = Deposit.objects.filter(is_deleted=False)
    serializer_class = DepositSerializer

class RetrieveDepositView(RetrieveAPIView):
    queryset = Deposit.objects.filter(is_deleted=False)
    serializer_class = DepositSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Deposit.DoesNotExist:
            raise NotFound({"error": "Deposit not found"})

class ConsultantExperienceListCreateAPIView(generics.GenericAPIView):
    queryset = ConsultantExperience.objects.filter(is_deleted=False)
    serializer_class = ConsultantExperienceBulkCreateSerializer

    def get(self, request, *args, **kwargs):
        experiences = self.get_queryset()
        serializer = ConsultantExperienceSerializer(experiences, many=True)
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
            serializer = ConsultantExperienceSerializer(data=experience_data)
            serializer.is_valid(raise_exception=True)
            experience = serializer.save()
            experiences.append(experience)

        response_serializer = ConsultantExperienceSerializer(experiences, many=True)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    
class ConsultantExperienceDetailAPIView(APIView):
    def get_object(self, pk):
        """Helper method to get the object by ID, handling soft deletes."""
        return get_object_or_404(ConsultantExperience, pk=pk, is_deleted=False)

    def get(self, request, pk, *args, **kwargs):
        """Retrieve a specific ConsultantExperience by ID."""
        experience = self.get_object(pk)
        serializer = ConsultantExperienceSerializer(experience)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        """Update a specific ConsultantExperience by ID."""
        experience = self.get_object(pk)
        serializer = ConsultantExperienceSerializer(experience, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, *args, **kwargs):
        """Soft delete a specific ConsultantExperience by ID."""
        experience = self.get_object(pk)
        experience.is_deleted = True
        experience.save()
        return Response({"detail": "Experience deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

class ConsultantExperienceRetrieveAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        """Retrieve a specific ConsultantExperience by ID."""
        experience = get_object_or_404(ConsultantExperience, pk=pk, is_deleted=False)
        serializer = ConsultantExperienceSerializer(experience)
        return Response(serializer.data)

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            name = serializer.validated_data['name']
            
            # Define email content
            subject = "Solicitud de registro - Sistema SNIA"
            from_email = 'noreply.snia@mmaya.gob.bo'
            recipient_list = [email]

            # Render HTML message
            context = {'name': name}
            html_message = render_to_string('email_templates/registration_email.html', context)
            plain_message = f"""
            Estimado/a {name},

            Hemos recibido su solicitud de inscripción en el Registro Nacional de Consultoría Ambiental (SNIA).
            Para completar su registro, entregue sus documentos en las oficinas del Ministerio de Medio Ambiente y Agua:
            
            Dirección: Av. 14 de septiembre No. 5397, esq. Calle 8 Obrajes, La Paz, Bolivia.
            
            Documentos requeridos:
            1. Nota de solicitud de inscripción dirigida a la Dirección General de Medio Ambiente y Cambios Climáticos, debidamente firmada por el solicitante, adjuntando el Formulario de Solicitud de Inscripción obtenido del Sistema Nacional de Información Ambiental (http://snia.mmaya.gob.bo), en calidad de Declaración Jurada.
            2. Copia de Título Profesional en Provisión Nacional, a nivel de Licenciatura o Técnico Superior Universitario. Los títulos otorgados en el exterior deben ser validados en su autenticidad por el Ministerio de Relaciones Exteriores.
            3. Copia de su cédula de identidad vigente.
            4. Comprobante de Depósito Bancario Original.

            Nota importante: Una vez validados sus documentos, recibirá un correo electrónico de confirmación indicando que puede recoger su certificado.

            Atentamente,
            SNIA - Ministerio de Medio Ambiente y Agua
            """

            # Send the email
            email = EmailMultiAlternatives(subject, plain_message, from_email, recipient_list)
            email.attach_alternative(html_message, "text/html")
            email.send()
            
            # Response to client
            return Response({'message': 'Solicitud enviada. Revise su correo electrónico para más detalles.'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ConsultantValidationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ConsultantValidationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Proceso de validación exitosa."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 

class ObservationAPIView(APIView):
    def post(self, request):
        serializer = ObservationSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            consultant = serializer.validated_data['consultant']
            rejection_reason = serializer.validated_data['rejection_reason']
            category = serializer.validated_data['category']

            # Define email content
            subject = "Observación en su registro - Sistema SNIA"
            from_email = 'noreply.snia@mmaya.gob.bo'
            recipient_list = [email]

            # Render HTML message
            context = {
                'consultant': consultant,
                'rejection_reason': rejection_reason,
                'category': category
            }
            html_message = render_to_string('email_templates/observation_email.html', context)
            plain_message = f"""
            Estimado/a {consultant},

            Lamentamos informarle que su inscripción al Registro Nacional de Consultoría Ambiental (SNIA) no pudo ser completada.

            Categoría solicitada: {category}

            Razón del rechazo: {rejection_reason}

            Por favor, revise los documentos enviados y realice las correcciones necesarias. Para más detalles, puede comunicarse con nuestras oficinas.

            Atentamente,
            SNIA - Ministerio de Medio Ambiente y Agua
            """

            # Send the email
            email = EmailMultiAlternatives(subject, plain_message, from_email, recipient_list)
            email.attach_alternative(html_message, "text/html")
            email.send()
            
            # Response to client
            return Response({'message': 'Correo de observación enviado correctamente.'}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
