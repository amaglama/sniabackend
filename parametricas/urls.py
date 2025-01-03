from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'parametricas', views.ParametricaViewSet, basename='parametricas')

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += router.urls
