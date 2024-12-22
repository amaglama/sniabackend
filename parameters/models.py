from django.db import models
from django.utils.timezone import now


class State(models.Model):
    name = models.CharField(max_length=25, unique=True) 
    code = models.CharField(max_length=10, null=True, blank=True)
    code_id = models.IntegerField(null=True, blank=True)  
    geographic_code = models.CharField(max_length=3, null=True, blank=True)  
    code_renca = models.CharField(max_length=10, null=True, blank=True)  
    code_renca_company = models.CharField(max_length=10, null=True, blank=True)  
    created_at = models.DateTimeField(default=now) 
    updated_at = models.DateTimeField(default=now)  
    is_deleted = models.BooleanField(default=False) 

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'states'

class Province(models.Model):
    province_code = models.CharField(max_length=10, unique=True)  # Código de la provincia
    province_name = models.CharField(max_length=255)  # Nombre de la provincia
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="provinces")  # Relación con estados
    created_at = models.DateTimeField(default=now)  # Fecha de creación
    updated_at = models.DateTimeField(default=now)  # Fecha de última modificación
    is_deleted = models.BooleanField(default=False)  # Indicador de eliminación lógica

    def __str__(self):
        return self.province_name

    class Meta:
        db_table = 'provinces'


class Municipality(models.Model):
    municipality_code = models.CharField(max_length=10, unique=True)  # Código del municipio
    ulot_name = models.CharField(max_length=255)  # Nombre del municipio (ULOT)
    ulot_capital_name = models.CharField(max_length=255, null=True, blank=True)  # Nombre del municipio (CAPITAL ULOT)
    ine_name = models.CharField(max_length=255, null=True, blank=True)  # Nombre del municipio (INE)
    mepf_name = models.CharField(max_length=255, null=True, blank=True)  # Nombre del municipio (MEFP)
    mepf_acronym = models.CharField(max_length=50, null=True, blank=True)  # Sigla del municipio (MEFP)
    mepf_code = models.CharField(max_length=50, null=True, blank=True)  # Código del municipio (MEFP)
    eta = models.CharField(max_length=50, null=True, blank=True)  # ETA
    tioc_aioc = models.CharField(max_length=255, null=True, blank=True)  # TIOC AIOC
    macroregion = models.CharField(max_length=255, null=True, blank=True)  # Macroregión
    observation = models.TextField(null=True, blank=True)  # Observación adicional
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name="municipalities")  # Relación con provincias
    created_at = models.DateTimeField(default=now)  # Fecha de creación
    updated_at = models.DateTimeField(default=now)  # Fecha de última modificación
    is_deleted = models.BooleanField(default=False)  # Indicador de eliminación lógica

    def __str__(self):
        return self.ulot_name

    class Meta:
        db_table = 'municipalities'
class BankAccount(models.Model):
    representative_name = models.CharField(max_length=150)
    account_name = models.CharField(max_length=150)
    unit_name = models.CharField(max_length=150)
    account_number = models.CharField(max_length=50, unique=True)
    bank_name = models.CharField(max_length=100)
    currency = models.CharField(max_length=10, default='BOB')
    state = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'bank_accounts'        

class Category(models.Model):
    name = models.CharField(max_length=255)
    registration_fee = models.DecimalField(max_digits=10, decimal_places=2)
    renewal_fee = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    abbreviation = models.CharField(max_length=1) # Sigla de la categoría (A, B, C)
    type = models.CharField(max_length=20)
    is_deleted = models.BooleanField(default=False) 
    class Meta:
        db_table = 'category'   

    def __str__(self):
        return self.name
