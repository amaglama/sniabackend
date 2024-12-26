from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, re_path,include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import protected_media_view

schema_view = get_schema_view(
    openapi.Info(
        title="Sistema Nacional de Informacion Ambiental  - SNIA",
        default_version='v1',
        description="Sistema de Seguimiento de Proyectos del Ministerio de Medio Ambiente y agua",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="sistemas@tu_api.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

selective_schema_view = get_schema_view(
    openapi.Info(
        title="Sistema Nacional de Informacion Ambiental  - SNIA",
        default_version='v1',
        description="Sistema de Seguimiento de Proyectos del Ministerio de Medio Ambiente y agua",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="sistemas@tu_api.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=[
        #path('api/', include('parametricas.urls')),
        #path('api/', include('consultants.urls')),
        path('api/', include('logs.urls')),
        path('o/', include('external.urls')),
    ],
)

project_schema_view = get_schema_view(
    openapi.Info(
        title="Sistema Nacional de Informacion Ambiental  - SNIA",
        default_version='v1',
        description="Sistema de Seguimiento de Proyectos del Ministerio de Medio Ambiente y agua",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="sistemas@tu_api.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=[
        #path('api/', include('parametricas.urls')),
        #path('api/', include('consultants.urls')),
        path('api/', include('logs.urls')),
        path('o/', include('external.urls')),
    ],
)


urlpatterns = [
    path('o/', include('external.urls', namespace='external')),
    path('admin/', admin.site.urls),
    path('protected-media/<path:file_path>/', protected_media_view, name='protected_media'),
    #path('media/', include('django.contrib.staticfiles.urls')),
    path('api/auth/',include('authentication.urls')),
    path('api/',include('parametros.urls_v2')),
    path('api/',include('administracion.urls_v2')),
    path('api/',include('parametricas.urls')),
    path('api/',include('consultants.urls')),
    path('api/',include('logs.urls')),
    path('api/',include('backend_mmaya.urls_lite')),
    path('api/',include('parameters.urls')),
    path('api/',include('consultants_renca.urls')),
    path('api/',include('announcements.urls')),

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
          ]