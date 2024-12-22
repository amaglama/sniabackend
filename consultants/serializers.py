from rest_framework import serializers
from .models import Consultant, Deposit, ConsultantExperience
from consultants_renca.models import ConsultantRenca, DepositRenca, ConsultantExperienceRenca
from consultants_renca.models import ConsultantRenca
from datetime import datetime
from django.db import transaction, IntegrityError
from django.shortcuts import get_object_or_404
from parameters.models import State, BankAccount
from django.db.models import Max



class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'

class BulkCreateDepositSerializer(serializers.Serializer):
    deposits = DepositSerializer(many=True)

    def create(self, validated_data):
        deposits_data = validated_data['deposits']
        deposits = [Deposit(**data) for data in deposits_data]
        return Deposit.objects.bulk_create(deposits)

class ConsultantExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultantExperience
        fields = '__all__'
class ConsultantExperienceBulkCreateSerializer(serializers.Serializer):
    experiences = serializers.ListField(
        child=serializers.DictField(),  # Cada experiencia debe ser un diccionario
        allow_empty=False,
        required=True
    )

    def create(self, validated_data):
        experiences_data = validated_data.pop('experiences', [])
        experiences = []
        for experience_data in experiences_data:
            experience = ConsultantExperience.objects.create(**experience_data)
            experiences.append(experience)
        return experiences

class DepositSerializer(serializers.ModelSerializer):
    """
    Serializador básico para manejar depósitos individuales.
    """
    consultant = serializers.PrimaryKeyRelatedField(queryset=Consultant.objects.all())
    bank_account = serializers.PrimaryKeyRelatedField(queryset=BankAccount.objects.all())

    class Meta:
        model = Deposit
        fields = '__all__'   

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'

class BulkCreateDepositSerializer(serializers.Serializer):
    deposits = DepositSerializer(many=True)

    def create(self, validated_data):
        deposits_data = validated_data['deposits']
        deposits = [Deposit(**data) for data in deposits_data]
        return Deposit.objects.bulk_create(deposits)


class ConsultantSerializer(serializers.ModelSerializer):
    experiences = ConsultantExperienceSerializer(many=True, read_only=True)
    deposits = DepositSerializer(many=True, read_only=True)
    photo_url = serializers.SerializerMethodField()
    state_certificate_doc_url = serializers.SerializerMethodField()
    identification_document_doc_url = serializers.SerializerMethodField()
    class Meta:
        model = Consultant
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

class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=255)
    category = serializers.ChoiceField(choices=[('A', 'Category A'), ('B', 'Category B'), ('C', 'Category C')])

class ConsultantValidationSerializer(serializers.Serializer):
    consultant_id = serializers.IntegerField()
    approved = serializers.BooleanField()
    verified_by = serializers.CharField(required=False)
    reason = serializers.CharField(required=False)

    def validate(self, data):
        """
        Custom validation to ensure that the consultant exists and reason is provided if not approved.
        """
        # Ensure consultant exists
        consultant_id = data.get('consultant_id')
        consultant = Consultant.objects.filter(id=consultant_id).first()
        if not consultant:
            raise serializers.ValidationError({"consultant_id": "The consultant with the given ID does not exist."})

        # Ensure reason is provided when not approved
        if not data['approved'] and not data.get('reason'):
            raise serializers.ValidationError({"reason": "Reason is required if the consultant is not approved."})
        
        return data
    
    def generate_renca_number(self, consultant_type, residence_id):
        """
        Generate the RENCA number based on consultant type and residence ID.
        """
        # Retrieve the state based on the residence ID
        state = State.objects.filter(id=residence_id).first()
        if not state:
            raise serializers.ValidationError({"residence": f"No code found for residence ID: {residence_id}"})

        # Determine the field based on the consultant type
        code_field = 'code_renca' if consultant_type == 'UNIPERSONAL NACIONAL' else 'code_renca_company'
        code_prefix = getattr(state, code_field, None)

        if not code_prefix:
            raise serializers.ValidationError({
                "consultant_type": f"No RENCA code prefix found for consultant type: {consultant_type}"
            })

        # Get the highest RENCA number associated with the prefix
        last_renca = ConsultantRenca.objects.filter(renca_number__startswith=code_prefix).aggregate(
            max_number=Max('renca_number')
        )['max_number']

        # Extract the number and calculate the next consecutive value
        if last_renca:
            last_number = int(last_renca[len(code_prefix):])
        else:
            last_number = 9000  # Start at 9000 if no previous records exist

        next_renca_number = f"{code_prefix}{last_number + 1}"
        return next_renca_number


    def save(self):
        """
        Handles the approval or rejection of a consultant. Copies data to ConsultantRenca if approved,
        or updates rejection details in Consultant. Updates related deposits and experiences' consultant_id if approved.
        """
        consultant_id = self.validated_data['consultant_id']
        
        # Fetch the consultant safely using get_object_or_404
        consultant = get_object_or_404(Consultant, id=consultant_id)

        if self.validated_data['approved']:
            # Handle approval: Copy data to ConsultantRenca and mark consultant as logically deleted
            with transaction.atomic():
                # Create ConsultantRenca record
                consultant_renca = ConsultantRenca.objects.create(
                    user_id=consultant.user_id,
                    state_consultant_renca="INSCRITO",
                    type_identification_document=consultant.type_identification_document,
                    identification_document=consultant.identification_document,
                    ci_complement=consultant.ci_complement,
                    ci_expedited=consultant.ci_expedited,
                    name=consultant.name,
                    last_name=consultant.last_name,
                    second_last_name=consultant.second_last_name,
                    residence_id=consultant.residence_id,
                    address=consultant.address,
                    telephone=consultant.telephone,
                    cellphone=consultant.cellphone,
                    email=consultant.email,
                    national_certificate=consultant.national_certificate,
                    state_certificate=consultant.state_certificate,
                    photo=consultant.photo,
                    state_certificate_doc=consultant.state_certificate_doc,
                    identification_document_doc=consultant.identification_document_doc,
                    renca_number=consultant.renca_number,
                    request_code=consultant.request_code,
                    emition_date=consultant.emition_date or datetime.now(),
                    consultant_type=consultant.consultant_type,
                    category=consultant.category,
                    visible_address=consultant.visible_address,
                    visible_telephone=consultant.visible_telephone,
                    visible_cellphone=consultant.visible_cellphone,
                    visible_email=consultant.visible_email,
                    state="INSCRITO",
                    verification_date=datetime.now(),
                    verified_by=self.validated_data.get('verified_by', 'System'),
                )

                # Mark the consultant as logically deleted
                consultant.is_deleted = True
                consultant.save()

                 # Copy deposits to DepositsRenca
                deposits = Deposit.objects.filter(consultant_id=consultant.id)
                for deposit in deposits:
                    DepositRenca.objects.create(
                        consultant=consultant_renca,
                        bank_account=deposit.bank_account,
                        amount=deposit.amount,
                        deposit_date=deposit.deposit_date,
                        reference_number=deposit.reference_number,
                        state=deposit.state,
                        created_at=deposit.created_at,
                        updated_at=deposit.updated_at,
                        is_deleted=deposit.is_deleted,
                    )

                # Copy experiences to ConsultantExperienceRenca
                experiences = ConsultantExperience.objects.filter(consultant_id=consultant.id)
                for experience in experiences:
                    ConsultantExperienceRenca.objects.create(
                        consultant=consultant_renca,
                        job_title=experience.job_title,
                        organization_name=experience.organization_name,
                        start_date=experience.start_date,
                        end_date=experience.end_date,
                        description=experience.description,
                        certificate_file=experience.certificate_file,
                        created_at=experience.created_at,
                        updated_at=experience.updated_at,
                        is_deleted=experience.is_deleted,
                    )

        else:
            # Handle rejection: Update rejection details
            consultant.rejection_reason = self.validated_data['reason']
            consultant.rejected_by = self.validated_data.get('verified_by', 'System')
            consultant.rejection_date = datetime.now()
            consultant.save()

class ObservationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    consultant = serializers.CharField(max_length=255)
    rejection_reason = serializers.CharField(max_length=500)
    category = serializers.ChoiceField(choices=[('A', 'Category A'), ('B', 'Category B'), ('C', 'Category C')])
