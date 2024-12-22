from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from parameters.models import State, BankAccount
from administracion.models import AuthUser


def upload_to_photos(instance, filename):
    """Genera la ruta de subida para el campo photo."""
    year = now().year
    ext = filename.split('.')[-1]  # extensión del archivo
    return f"consultants/photos/{year}/{instance.renca_number}.{ext}"

def upload_to_docs(instance, filename):
    """Genera la ruta de subida para el titulo en provision."""
    year = now().year
    ext = filename.split('.')[-1]
    return f"consultants/docs/{year}/{instance.renca_number}.{ext}"

def upload_to_identifications(instance, filename):
    """Genera la ruta de subida para el documento de identificación."""
    year = now().year
    ext = filename.split('.')[-1]
    return f"consultants/identifications/{year}/{instance.renca_number}.{ext}"

def upload_to_certificates(instance, filename):
    """Genera la ruta de subida para los certificados de experiencia."""
    year = now().year
    ext = filename.split('.')[-1]  # Obtén la extensión del archivo
    return f"consultants/experience/{year}/{instance.id or 'temp'}.{ext}"

class Consultant(models.Model):
    TYPE_IDENTIFICATION_CHOICES = [
        ('CI', 'CÉDULA DE IDENTIDAD'),
        ('CI EXTRANJERA', 'CÉDULA DE IDENTIDAD EXTRANJERA'),
        ('PASAPORTE', 'PASSPORT')
    ]
    CONSULTANT_TYPE_CHOICES = [
        ('UNIPERSONAL NACIONAL', 'Unipersonal Nacional'),
        ('UNIPERSONAL EXTRANJERA', 'Unipersonal Extranjera')
    ]
    CATEGORY_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C')
    ]

    user_id = models.ForeignKey(AuthUser, on_delete=models.CASCADE, db_column='user_id', null=True, blank=True)  # Clave foránea
    state_consultant = models.CharField(max_length=15, default='INSCRITO')  # Campo con valor predeterminado
    type_identification_document = models.CharField(max_length=50, choices=TYPE_IDENTIFICATION_CHOICES)
    identification_document = models.CharField(max_length=50)
    ci_complement = models.CharField(max_length=10, blank=True, null=True)
    ci_expedited = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    second_last_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=300)
    residence_id = models.ForeignKey(State, on_delete=models.SET_NULL, db_column='residence_id', null=True, blank=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    cellphone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=150, unique=True)
    national_certificate = models.CharField(max_length=50, blank=True, null=True)
    state_certificate = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImageField(upload_to=upload_to_photos, blank=True, null=True)
    state_certificate_doc = models.FileField(upload_to=upload_to_docs, blank=True, null=True)
    identification_document_doc = models.FileField(upload_to=upload_to_identifications, blank=True, null=True)
    renca_number = models.CharField(max_length=50, unique=True, blank=True, null=True) 
    request_code = models.CharField(max_length=50, unique=True, blank=True, null=True)
    emition_date = models.DateTimeField(default=now)
    consultant_type = models.CharField(max_length=50, choices=CONSULTANT_TYPE_CHOICES)
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default='A')
    visible_address = models.BooleanField(default=True)
    visible_telephone = models.BooleanField(default=True)
    visible_cellphone = models.BooleanField(default=True)
    visible_email = models.BooleanField(default=True)
    rejection_reason = models.TextField(blank=True, null=True)  # Observaciones del rechazo
    rejected_by = models.CharField(max_length=150, blank=True, null=True)  # Usuario que rechazó
    rejection_date = models.DateTimeField(blank=True, null=True)  # Fecha del rechazo
    state = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    class Meta:
        db_table = 'consultants'

class Deposit(models.Model):
    consultant = models.ForeignKey(
        'Consultant',
        on_delete=models.CASCADE,
        related_name='deposits',
        db_column='consultant_id'
    )
    bank_account = models.ForeignKey(
        'parameters.BankAccount',
        on_delete=models.CASCADE,
        related_name='deposits',
        db_column='bank_account_id'
    )
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    deposit_date = models.DateTimeField()
    reference_number = models.CharField(max_length=100)
    state = models.CharField(
        max_length=50,
        default='PENDING'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    class Meta:
        db_table = 'deposits'

class ConsultantExperience(models.Model):
    consultant = models.ForeignKey(
        Consultant,
        on_delete=models.CASCADE,
        related_name='experiences',
        db_column='consultant_id'
    )
    job_title = models.CharField(max_length=150)
    organization_name = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    certificate_file = models.FileField(upload_to=upload_to_certificates, blank=True, null=True)  # Nuevo campo
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'consultant_experience'