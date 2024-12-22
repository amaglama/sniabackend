from rest_framework import serializers
from .models import ConsultantRenca, DepositRenca, ConsultantExperienceRenca
from consultants.models import Consultant
from parameters.models import BankAccount
from datetime import datetime
from django.db import transaction, IntegrityError
from django.shortcuts import get_object_or_404
from parameters.models import State
from django.db.models import Max


class DepositRencaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositRenca
        fields = '__all__'

class BulkCreateDepositSerializer(serializers.Serializer):
    deposits = DepositRencaSerializer(many=True)

    def create(self, validated_data):
        deposits_data = validated_data['deposits']
        deposits = [DepositRenca(**data) for data in deposits_data]
        return DepositRenca.objects.bulk_create(deposits)

class ConsultantExperienceRencaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultantExperienceRenca
        fields = '__all__'
class ConsultantExperienceRencaBulkCreateSerializer(serializers.Serializer):
    experiences = serializers.ListField(
        child=serializers.DictField(),  # Cada experiencia debe ser un diccionario
        allow_empty=False,
        required=True
    )

    def create(self, validated_data):
        experiences_data = validated_data.pop('experiences', [])
        experiences = []
        for experience_data in experiences_data:
            experience = ConsultantExperienceRenca.objects.create(**experience_data)
            experiences.append(experience)
        return experiences

class DepositRencaSerializer(serializers.ModelSerializer):
    """
    Serializador básico para manejar depósitos individuales.
    """
    consultant = serializers.PrimaryKeyRelatedField(queryset=Consultant.objects.all())
    bank_account = serializers.PrimaryKeyRelatedField(queryset=BankAccount.objects.all())

    class Meta:
        model = DepositRenca
        fields = '__all__'   

class DepositRencaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositRenca
        fields = '__all__'

class BulkCreateDepositRencaSerializer(serializers.Serializer):
    deposits = DepositRencaSerializer(many=True)

    def create(self, validated_data):
        deposits_data = validated_data['deposits']
        deposits = [DepositRenca(**data) for data in deposits_data]
        return DepositRenca.objects.bulk_create(deposits)


class ConsultantRencaSerializer(serializers.ModelSerializer):
    experiences = ConsultantExperienceRencaSerializer(many=True, read_only=True)
    deposits = DepositRencaSerializer(many=True, read_only=True)
    photo_url = serializers.SerializerMethodField()
    state_certificate_doc_url = serializers.SerializerMethodField()
    identification_document_doc_url = serializers.SerializerMethodField()
    class Meta:
        model = ConsultantRenca
        fields = '__all__'
    
    def get_photo_url(self, obj):
        if obj.photo:
            request = self.context.get('request')
            return request.build_absolute_uri(f'/protected-media/{obj.photo.name}')
        return None

    def get_state_certificate_doc_url(self, obj):
        if obj.state_certificate_doc:
            request = self.context.get('request')
            return request.build_absolute_uri(f'/protected-media/{obj.state_certificate_doc.name}')
        return None

    def get_identification_document_doc_url(self, obj):
        if obj.identification_document_doc:
            request = self.context.get('request')
            return request.build_absolute_uri(f'/protected-media/{obj.identification_document_doc.name}')
        return None



    


    
