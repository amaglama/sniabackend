------------------------ {'default': {'ENGINE': 'django.db.backends.postgresql', 'NAME': 'waradb_v2', 'USER': 'postgres', 'PASSWORD': 'postgres', 'HOST': '127.0.0.1', 'PORT': '5432'}}
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actions(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actions'


class AgenciaFinanciadora(models.Model):
    id = models.SmallAutoField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    sigla = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agencia_financiadora'


class Areas(models.Model):
    nombre = models.CharField(unique=True, max_length=255, blank=True, null=True)
    estado = models.TextField(blank=True, null=True)  # This field type is a guess.
    ministerio = models.ForeignKey('Ministerios', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('AuthUser', models.DO_NOTHING, related_name='areas_updated_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areas'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)

class AuthUser(models.Model):
    TYPE_IDENTIFICATION_CHOICES = [
        ('CI', 'CÉDULA DE IDENTIDAD'),
        ('CI EXTRANJERA', 'CÉDULA DE IDENTIDAD EXTRANJERA'),
        ('PASAPORTE', 'PASSPORT')
    ]
   
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    second_last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=128)

    type_identification_document = models.CharField(max_length=50, choices=TYPE_IDENTIFICATION_CHOICES)
    identification_document = models.CharField(max_length=50)
    ci_complement = models.CharField(max_length=10, blank=True, null=True)
    ci_expedited = models.CharField(max_length=50, blank=True, null=True)
    cellphone = models.CharField(max_length=20, blank=True, null=True)

    is_staff = models.BooleanField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(blank=True, null=True)
    date_joined = models.DateTimeField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)  # This field type is a guess.
    #cargo = models.ForeignKey('Cargos', models.DO_NOTHING, blank=True, null=True)
    #viceministerio = models.ForeignKey('Viceministerios', models.DO_NOTHING, blank=True, null=True)
    #descentralizada = models.ForeignKey('Ejecutores', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_by = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('self', models.DO_NOTHING, related_name='authuser_updated_by_set', blank=True, null=True)
    #tipo = models.TextField()  # This field type is a guess.
    #sector = models.ForeignKey('Sectores', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserCopy1(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    second_last_name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user_copy1'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Cargos(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    estructura_organizativa = models.ForeignKey('EstructurasOrganizativas', models.DO_NOTHING)
    denominacion_cargo = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cargos'


class CoEjecutores(models.Model):
    id = models.SmallAutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    estado = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='coejecutores_updated_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'co_ejecutores'


class Comunidades(models.Model):
    nombre = models.CharField(max_length=760)
    municipio = models.ForeignKey('Municipios', models.DO_NOTHING)
    estado = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='comunidades_updated_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comunidades'


class Departamentos(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='departamentos_updated_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamentos'


class Descentralizadas(models.Model):
    nombre = models.CharField(unique=True, max_length=255)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'descentralizadas'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DocumentoRespaldo(models.Model):
    id = models.SmallAutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documento_respaldo'


class DrenajesPluviales(models.Model):
    proyecto = models.OneToOneField('Proyectos', models.DO_NOTHING, blank=True, null=True)
    familias_beneficiadas = models.IntegerField(blank=True, null=True)
    poblacion_beneficiada = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drenajes_pluviales'


class Ejecutores(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='ejecutores_updated_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ejecutores'


class EmpresasConstructoras(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='empresasconstructoras_updated_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresas_constructoras'


class Estados2(models.Model):
    nombre = models.CharField(unique=True, max_length=255)
    estado = models.TextField()  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados2'


class EstadosDetallados2(models.Model):
    estado = models.ForeignKey(Estados2, models.DO_NOTHING, blank=True, null=True)
    nombre = models.CharField(max_length=255)
    observacion = models.TextField(blank=True, null=True)
    estado_0 = models.TextField(db_column='estado')  # Field renamed because of name conflict. This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados_detallados2'
        unique_together = (('estado', 'nombre'),)


class EstadosPreinversion(models.Model):
    nombre = models.CharField(unique=True, max_length=50)
    estado = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='estadospreinversion_updated_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados_preinversion'


class EstructurasOrganizativas(models.Model):
    nombre = models.CharField(unique=True, max_length=255, blank=True, null=True)
    estado = models.TextField(blank=True, null=True)  # This field type is a guess.
    area = models.ForeignKey(Areas, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='estructurasorganizativas_updated_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estructuras_organizativas'


class Gobiernos(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='gobiernos_updated_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gobiernos'


class GroupMenu(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    menu = models.ForeignKey('Menu', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'group_menu'
        unique_together = (('group', 'menu'),)


class KnoxAuthtoken(models.Model):
    digest = models.CharField(primary_key=True, max_length=128)
    created = models.DateTimeField()
    user_id = models.IntegerField()
    expiry = models.DateTimeField(blank=True, null=True)
    token_key = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'knox_authtoken'


class Lugares(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    estado = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='lugares_updated_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lugares'


class Menu(models.Model):
    ruta = models.CharField(max_length=255)
    icono = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    grupo = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    menu_padre = models.ForeignKey('MenuPadre', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'


class MenuPadre(models.Model):
    nombre_menu = models.CharField(max_length=100, blank=True, null=True)
    icono = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_padre'

"""
class MetaPreinversion(models.Model):
    preinversion = models.ForeignKey('ProyectosPreinversion', models.DO_NOTHING)
    meta = models.ForeignKey('Metas', models.DO_NOTHING)
    valor = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_preinversion'


class Metas(models.Model):
    titulo = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metas'

"""
class Ministerios(models.Model):
    nombre = models.CharField(unique=True, max_length=255)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ministerios'


class Municipios(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    provincia = models.ForeignKey('Provincias', models.DO_NOTHING, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='municipios_updated_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipios'


class Oauth2ProviderAccesstoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(unique=True, max_length=255)
    expires = models.DateTimeField()
    scope = models.TextField()
    application = models.ForeignKey('Oauth2ProviderApplication', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    source_refresh_token = models.OneToOneField('Oauth2ProviderRefreshtoken', models.DO_NOTHING, blank=True, null=True)
    id_token = models.OneToOneField('Oauth2ProviderIdtoken', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth2_provider_accesstoken'


class Oauth2ProviderApplication(models.Model):
    id = models.BigAutoField(primary_key=True)
    client_id = models.CharField(unique=True, max_length=100)
    redirect_uris = models.TextField()
    client_type = models.CharField(max_length=32)
    authorization_grant_type = models.CharField(max_length=32)
    client_secret = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    skip_authorization = models.BooleanField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    algorithm = models.CharField(max_length=5)
    post_logout_redirect_uris = models.TextField()
    hash_client_secret = models.BooleanField()
    allowed_origins = models.TextField()

    class Meta:
        managed = False
        db_table = 'oauth2_provider_application'


class Oauth2ProviderGrant(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=255)
    expires = models.DateTimeField()
    redirect_uri = models.TextField()
    scope = models.TextField()
    application = models.ForeignKey(Oauth2ProviderApplication, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    code_challenge = models.CharField(max_length=128)
    code_challenge_method = models.CharField(max_length=10)
    nonce = models.CharField(max_length=255)
    claims = models.TextField()

    class Meta:
        managed = False
        db_table = 'oauth2_provider_grant'


class Oauth2ProviderIdtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    jti = models.UUIDField(unique=True)
    expires = models.DateTimeField()
    scope = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    application = models.ForeignKey(Oauth2ProviderApplication, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth2_provider_idtoken'


class Oauth2ProviderRefreshtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(max_length=255)
    access_token = models.OneToOneField(Oauth2ProviderAccesstoken, models.DO_NOTHING, blank=True, null=True)
    application = models.ForeignKey(Oauth2ProviderApplication, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    revoked = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth2_provider_refreshtoken'
        unique_together = (('token', 'revoked'),)



class OrganizacionesFinancieras(models.Model):
    sigla = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='organizacionesfinancieras_updated_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organizaciones_financieras'


class Programas(models.Model):
    viceministerio = models.TextField(blank=True, null=True)
    entidad_ejecutora = models.TextField(blank=True, null=True)
    co_ejecutor = models.TextField(blank=True, null=True)
    programas_proyectos = models.TextField(blank=True, null=True)
    sigla_prog_convenio = models.TextField(blank=True, null=True)
    agencia_financiadora = models.TextField(blank=True, null=True)
    descripcion_agencia_financiadora = models.TextField(blank=True, null=True)
    tipo_convenio = models.TextField(blank=True, null=True)
    documento_respaldo = models.TextField(blank=True, null=True)
    codigo_convenio = models.CharField(max_length=100, blank=True, null=True)
    enlace_convenio = models.TextField(blank=True, null=True)
    #tipo_financiamiento = models.TextField(blank=True, null=True)
    departamentos_field = models.TextField(db_column='departamentos_', blank=True, null=True)  # Field renamed because it ended with '_'.
    municpios = models.TextField(blank=True, null=True)
    sector = models.TextField(blank=True, null=True)
    subsector = models.TextField(blank=True, null=True)
    fecha_suscripcion_convenio_contrato = models.TextField(blank=True, null=True)
    fecha_vencimiento = models.TextField(blank=True, null=True)
    nueva_fecha_vencimiento = models.TextField(blank=True, null=True)
    hoy = models.TextField(blank=True, null=True)
    vigente_no_vigente = models.TextField(blank=True, null=True)
    estructura_financiera = models.TextField(blank=True, null=True)
    enlace_estructura_financiera = models.TextField(blank=True, null=True)
    componentes_field = models.TextField(db_column='componentes_', blank=True, null=True)  # Field renamed because it ended with '_'.
    enlace_componentes = models.TextField(blank=True, null=True)
    desembolsos = models.TextField(blank=True, null=True)
    enlace_desembolsos = models.TextField(blank=True, null=True)
    ejecucion_programa_fuente_externa = models.TextField(blank=True, null=True)
    enlace_ejecucion_del_programa_fuente_externa = models.TextField(blank=True, null=True)
    ejecucion_del_programa_contraparte_local = models.TextField(blank=True, null=True)
    enlace_ejecucion_del_programa_contraparte_local = models.TextField(blank=True, null=True)
    proyectos_inversion = models.TextField(blank=True, null=True)
    enlace_proyectos_inversion = models.TextField(blank=True, null=True)
    #proyectos_preinversion = models.TextField(blank=True, null=True)
    #enlace_proyectos_preinversion = models.TextField(blank=True, null=True)
    superficies_bajo_riego_ha = models.TextField(blank=True, null=True)
    enlace_superficies_bajo_riego_ha = models.TextField(blank=True, null=True)
    manejo_integral_cuencas_km2 = models.TextField(blank=True, null=True)
    n_ptap = models.TextField(blank=True, null=True)
    n_ptar = models.TextField(blank=True, null=True)
    n_habitantes_con_acceso_a_saneamiento_basico = models.TextField(blank=True, null=True)
    otros = models.TextField(blank=True, null=True)
    enlace_otros = models.TextField(blank=True, null=True)
    indicadores_programa_psdi_pdes = models.TextField(blank=True, null=True)
    estado_situacion_programa_field = models.TextField(db_column='estado_situacion_programa_', blank=True, null=True)  # Field renamed because it ended with '_'.
    detallado_descripcion = models.TextField(blank=True, null=True)
    detallado_codigo = models.CharField(max_length=255, blank=True, null=True)
    estado = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_by_id = models.IntegerField(blank=True, null=True)
    updated_by_id = models.IntegerField(blank=True, null=True)
    tipo_migrado = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programas'


class Provincias(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    departamento = models.ForeignKey(Departamentos, models.DO_NOTHING, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='provincias_updated_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provincias'


class Proyectos(models.Model):
    lugar = models.ForeignKey(Lugares, models.DO_NOTHING, blank=True, null=True)
    sector = models.ForeignKey('Sectores', models.DO_NOTHING, blank=True, null=True)
    nombre = models.CharField(max_length=1255, blank=True, null=True)
    organizacion = models.ForeignKey(OrganizacionesFinancieras, models.DO_NOTHING, blank=True, null=True)
    ejecutor = models.ForeignKey(Ejecutores, models.DO_NOTHING, blank=True, null=True)
    tipo = models.ForeignKey('TiposProyecto', models.DO_NOTHING, blank=True, null=True)
    detalle = models.TextField(blank=True, null=True)
    estado_detallado = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_conclusion = models.DateField(blank=True, null=True)
    programa = models.ForeignKey(Programas, models.DO_NOTHING, blank=True, null=True)
    poblacion_beneficiaria_cuencas = models.CharField(max_length=100, blank=True, null=True)
    numero_familias_beneficiadas = models.IntegerField(blank=True, null=True)
    numero_familias_indirectas = models.IntegerField(blank=True, null=True)
    toneladas_residuos_dispuestos_anio = models.FloatField(blank=True, null=True)
    toneladas_residuos_aprovechamiento_anio = models.FloatField(blank=True, null=True)
    superficie_riego_ha = models.FloatField(blank=True, null=True)
    hectareas_bajo_riego = models.IntegerField(blank=True, null=True)
    hectareas_reforestadas = models.IntegerField(blank=True, null=True)
    sistemas_riego = models.FloatField(blank=True, null=True)
    numero_plantines = models.IntegerField(blank=True, null=True)
    forestacion_ha = models.IntegerField(blank=True, null=True)
    reforestacion_ha = models.IntegerField(blank=True, null=True)
    superficie_plantada = models.IntegerField(blank=True, null=True)
    viveros = models.IntegerField(blank=True, null=True)
    empleos_directos = models.IntegerField(blank=True, null=True)
    empleos_indirectos = models.IntegerField(blank=True, null=True)
    empresa_constructora = models.ForeignKey(EmpresasConstructoras, models.DO_NOTHING, blank=True, null=True)
    proyecto_cuenta_con_ptar = models.CharField(max_length=50, blank=True, null=True)
    proyectos_con_sin_represa = models.CharField(max_length=50, blank=True, null=True)
    ucep_responsable = models.ForeignKey('UcepResponsables', models.DO_NOTHING, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    conclusion = models.DateField(blank=True, null=True)
    gobierno = models.CharField(max_length=50, blank=True, null=True)
    obs_fechaini_fechafin = models.CharField(db_column='obs_fechaIni_fechaFin', max_length=255, blank=True, null=True)  # Field name made lowercase.
    obs_avance = models.CharField(max_length=255, blank=True, null=True)
    obs_poblacion_beneficiara = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    fecha_inicio_cif = models.DateField(blank=True, null=True)
    fecha_fin_cif = models.DateField(blank=True, null=True)
    beneficiados_varones = models.IntegerField(blank=True, null=True)
    beneficiados_mujeres = models.IntegerField(blank=True, null=True)
    total_programado_2024 = models.FloatField(blank=True, null=True)
    #objetivo = models.TextField(blank=True, null=True)
    programado_para_entrega_por_efemeride = models.TextField(blank=True, null=True)
    estado_reportado_por_el_sector_para_efemeride = models.TextField(blank=True, null=True)
    viceministerio = models.ForeignKey('Viceministerios', models.DO_NOTHING, blank=True, null=True)
    emblematico = models.BooleanField(blank=True, null=True)
    gestion = models.IntegerField(blank=True, null=True)
    estado = models.ForeignKey(Estados2, models.DO_NOTHING, blank=True, null=True)
    tipo_migrado = models.CharField(max_length=255, blank=True, null=True)
    codigo_sisin = models.CharField(max_length=50)
    latitud = models.CharField(max_length=100, blank=True, null=True)
    longitud = models.CharField(max_length=100, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    documento_creacion = models.CharField(max_length=255, blank=True, null=True)
    imagen_proyecto = models.CharField(max_length=255, blank=True, null=True)
    sector_clasificador = models.ForeignKey('SectoresClasificador', models.DO_NOTHING, blank=True, null=True)
    sub_sector_clasificador = models.ForeignKey('SubSectoresClasificador', models.DO_NOTHING, blank=True, null=True)
    estado_detallado_nuevo = models.ForeignKey(EstadosDetallados2, models.DO_NOTHING, blank=True, null=True)
    tipo_proyecto_detallado = models.CharField(max_length=700, blank=True, null=True)
    tipo_conflicto = models.CharField(max_length=255, blank=True, null=True)
    descripcion_conflicto = models.CharField(max_length=255, blank=True, null=True)
    codigo_convenio = models.CharField(max_length=100, blank=True, null=True)
    preinversion = models.ForeignKey('ProyectosPreinversion', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyectos'

class RealizacionDepartamentos(models.Model):
    realizacion = models.ForeignKey('Realizaciones', models.DO_NOTHING, blank=True, null=True)
    departamento = models.ForeignKey(Departamentos, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'realizacion_departamentos'


class RealizacionMunicipios(models.Model):
    id = models.SmallAutoField(primary_key=True)
    realizacion = models.ForeignKey('Realizaciones', models.DO_NOTHING, blank=True, null=True)
    municipio = models.ForeignKey(Municipios, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'realizacion_municipios'


class RealizacionProvincias(models.Model):
    id = models.SmallAutoField(primary_key=True)
    realizacion = models.ForeignKey('Realizaciones', models.DO_NOTHING, blank=True, null=True)
    provincia = models.ForeignKey(Provincias, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'realizacion_provincias'


class Realizaciones(models.Model):
    proyecto = models.OneToOneField(Proyectos, models.DO_NOTHING, blank=True, null=True)
    departamento = models.ForeignKey(Departamentos, models.DO_NOTHING, blank=True, null=True)
    provincia = models.ForeignKey(Provincias, models.DO_NOTHING, blank=True, null=True)
    municipio = models.ForeignKey(Municipios, models.DO_NOTHING, blank=True, null=True)
    total_inversion = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    avance_fisico = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    avance_financiamiento = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    inversion_presupuestada = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    saldo_presupuesto = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    fecha_concl_obra = models.DateField(blank=True, null=True)
    conclusion_concl_proy = models.DateField(blank=True, null=True)
    contraparte_local = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    contraparte_local_no_financiera = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    contratado = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    eje_acum = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    proyecto_cuenta_con_ptar = models.CharField(max_length=50, blank=True, null=True)
    financiamiento_externo = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    gad = models.FloatField(blank=True, null=True)
    gad_no_financiero = models.FloatField(blank=True, null=True)
    presupuesto_vapsb = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    total_ejecutado_acumulado_bs_2023 = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    total_ejecutado_mill_bs_2023 = models.IntegerField(blank=True, null=True)
    total_inversion_mill = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    responsable_contraparte = models.ForeignKey('ResponsablesContraparte', models.DO_NOTHING, blank=True, null=True)
    ejecutor = models.ForeignKey(Ejecutores, models.DO_NOTHING, blank=True, null=True)
    org_financ = models.ForeignKey(OrganizacionesFinancieras, models.DO_NOTHING, blank=True, null=True)
    programa = models.ForeignKey(Programas, models.DO_NOTHING, blank=True, null=True)
    tipo_de_proyecto = models.ForeignKey('TiposProyecto', models.DO_NOTHING, blank=True, null=True)
    ucep_responsable = models.ForeignKey('UcepResponsables', models.DO_NOTHING, blank=True, null=True)
    lugar = models.ForeignKey(Lugares, models.DO_NOTHING, blank=True, null=True)
    estado = models.ForeignKey(Estados2, models.DO_NOTHING, blank=True, null=True)
    bol = models.FloatField(blank=True, null=True)
    ppcr = models.FloatField(blank=True, null=True)
    financiamiento_pnc = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'realizaciones'


class ResponsablesContraparte(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    estado = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='responsablescontraparte_updated_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'responsables_contraparte'


class SectorEjecutor(models.Model):
    sector = models.ForeignKey('Sectores', models.DO_NOTHING, blank=True, null=True)
    ejecutor = models.ForeignKey(Ejecutores, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sector_ejecutor'


class SectorLugar(models.Model):
    sector = models.ForeignKey('Sectores', models.DO_NOTHING, blank=True, null=True)
    lugar = models.ForeignKey(Lugares, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sector_lugar'


class SectorPrograma(models.Model):
    sector = models.ForeignKey('Sectores', models.DO_NOTHING, blank=True, null=True)
    programa = models.ForeignKey(Programas, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sector_programa'


class Sectores(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='sectores_updated_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sectores'


class SectoresClasificador(models.Model):
    nombre = models.CharField(unique=True, max_length=255)
    estado = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sectores_clasificador'


class Seguimiento(models.Model):
    id = models.SmallAutoField(primary_key=True)
    realizacion = models.ForeignKey(Realizaciones, models.DO_NOTHING, blank=True, null=True)
    proyecto_id = models.SmallIntegerField(blank=True, null=True)
    mes = models.CharField(max_length=20, blank=True, null=True)
    anio = models.CharField(max_length=20, blank=True, null=True)
    total_programado_proyecto = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    avance_financiero_mes = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    porcentaje_avance_financiero_mes = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    porcentaje_resto_financiero_mes = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    porcentaje_avance_fisico_mes = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    porcentaje_resto_fisico_mes = models.CharField(max_length=255, blank=True, null=True)
    fotografia_1 = models.CharField(max_length=255, blank=True, null=True)
    fotografia_2 = models.CharField(max_length=255, blank=True, null=True)
    fotografia_3 = models.CharField(max_length=255, blank=True, null=True)
    fotografia_4 = models.CharField(max_length=255, blank=True, null=True)
    documento_respaldo_avance = models.CharField(max_length=255, blank=True, null=True)
    fecha_actualizacion_avance = models.DateTimeField(blank=True, null=True)
    detalle_seguimiento = models.TextField(blank=True, null=True)
    acumulado_financiero_mes = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    acumulado_porcentaje_financiero_mes = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    acumulado_porcentaje_fisico_mes = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    estado_proyecto = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by_id = models.IntegerField(blank=True, null=True)
    update_by_id = models.IntegerField(blank=True, null=True)
    saldo_programado_proyecto = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    estado_seguimiento = models.CharField(max_length=30, blank=True, null=True)
    observacion_estado = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seguimiento'


class SubSector(models.Model):
    id = models.SmallAutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_sector'


class SubSectoresClasificador(models.Model):
    nombre = models.CharField(unique=True, max_length=255)
    sector_clasificador = models.ForeignKey(SectoresClasificador, models.DO_NOTHING, blank=True, null=True)
    estado = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_sectores_clasificador'








class TiposPrograma(models.Model):
    nombre = models.CharField(unique=True, max_length=255)
    estado = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='tiposprograma_updated_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_programa'

"""
class TiposProyecto(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='tiposproyecto_updated_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_proyecto'


class TiposProyectoPreinversion(models.Model):
    nombre = models.CharField(unique=True, max_length=50)
    estado = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='tiposproyectopreinversion_updated_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_proyecto_preinversion'
"""

class UcepResponsables(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='ucepresponsables_updated_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ucep_responsables'


class UserActions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    action = models.ForeignKey(Actions, models.DO_NOTHING, blank=True, null=True)
    resource = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    extra = models.CharField(max_length=255, blank=True, null=True)
    resource_affected = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_actions'


class UserMenu(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    menu = models.ForeignKey(Menu, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_menu'
        unique_together = (('user_id', 'menu'),)


class ViceministerioDescentralizada(models.Model):
    viceministerio = models.ForeignKey('Viceministerios', models.DO_NOTHING)
    descentralizada = models.ForeignKey(Ejecutores, models.DO_NOTHING)
    id = models.AutoField()

    class Meta:
        managed = False
        db_table = 'viceministerio_descentralizada'
        unique_together = (('viceministerio', 'descentralizada'),)

""" 
class ViceministerioSector(models.Model):
    viceministerio = models.ForeignKey('Viceministerios', models.DO_NOTHING)
    sector = models.ForeignKey(Sectores, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'viceministerio_sector'
        unique_together = (('viceministerio', 'sector'),)
"""

class Viceministerios(models.Model):
    id = models.SmallAutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    estado = models.TextField()  # This field type is a guess.
    ministerio = models.ForeignKey(Ministerios, models.DO_NOTHING, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'viceministerios'
