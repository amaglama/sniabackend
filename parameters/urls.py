from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StateListCreateView, StateRetrieveUpdateDestroyView, BankAccountViewSet, CategoryViewSet
from .views import (
    ProvinceListCreateView,
    ProvinceRetrieveUpdateDestroyView,
    MunicipalityListCreateView,
    MunicipalityRetrieveUpdateDestroyView,
    StateProvincesMunicipalitiesView,
    MunicipalityReverseLookupView,
    StateCascadeView, ProvinceCascadeView, MunicipalityCascadeView
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category'),
router.register(r'bank-accounts', BankAccountViewSet, basename='bank-accounts')

urlpatterns = [
    path('states/', StateListCreateView.as_view(), name='state-list-create'),
    path('states/<int:pk>/', StateRetrieveUpdateDestroyView.as_view(), name='state-detail'),
    path('', include(router.urls)),  # Incluye las rutas del enrutador

# Province endpoints
    path('provinces/', ProvinceListCreateView.as_view(), name='province-list-create'),
    path('provinces/<int:pk>/', ProvinceRetrieveUpdateDestroyView.as_view(), name='province-detail'),

    # Municipality endpoints
    path('municipalities/', MunicipalityListCreateView.as_view(), name='municipality-list-create'),
    path('municipalities/<int:pk>/', MunicipalityRetrieveUpdateDestroyView.as_view(), name='municipality-detail'),

    # se envia el state y devuelve toda la info de provincias y municipios
    path('states/<int:state_id>/provinces-municipalities/', StateProvincesMunicipalitiesView.as_view(), name='state-provinces-municipalities'),

    # Reverse lookup se envia el id municipe y devuelve provincia y state, todo
    path('municipalities/<int:pk>/reverse/', MunicipalityReverseLookupView.as_view(), name='municipality-reverse-lookup'),

    # combos cascada
    path('states/cascade/', StateCascadeView.as_view(), name='state-cascade'),
    path('states/<int:state_id>/provinces/', ProvinceCascadeView.as_view(), name='province-cascade'),
    path('provinces/<int:province_id>/municipalities/', MunicipalityCascadeView.as_view(), name='municipality-cascade'),
]