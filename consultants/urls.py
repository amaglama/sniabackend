from django.urls import path
from .views import (
    ConsultantListCreateAPIView, ConsultantRetrieveUpdateDestroyAPIView,
    ConsultantExperienceRetrieveAPIView,RetrieveDepositView,
    ConsultantExperienceListCreateAPIView, BulkCreateDepositView, EditDepositView, DeleteDepositView, ListDepositsView, RegisterAPIView,
    ConsultantValidationView,ObservationAPIView,
)
from .views import ConsultantExperienceListCreateAPIView, ConsultantExperienceDetailAPIView

urlpatterns = [
    path('consultants/', ConsultantListCreateAPIView.as_view(), name='consultant-list-create'),
    path('consultants/<int:pk>/', ConsultantRetrieveUpdateDestroyAPIView.as_view(), name='consultant-detail'),
    path('deposits/', ListDepositsView.as_view(), name='deposits_list'),
    path('deposits/<int:pk>/', RetrieveDepositView.as_view(), name='deposit_detail'),
    path('deposits/bulk/create/', BulkCreateDepositView.as_view(), name='deposits_bulk_create'),
    path('deposits/edit/<int:pk>/', EditDepositView.as_view(), name='deposit_edit'),
    path('deposits/delete/<int:pk>/', DeleteDepositView.as_view(), name='deposit_delete'),
    path('experiencesssss/', ConsultantExperienceListCreateAPIView.as_view(), name='experience-list'),
    path('experiences/<int:pk>/', ConsultantExperienceRetrieveAPIView.as_view(), name='consultant-experience-detail'),
    path('experiences/bulk/create/', ConsultantExperienceListCreateAPIView.as_view(), name='experiences-bulk-list-create'),
    path('experiences/edit/<int:pk>/', ConsultantExperienceDetailAPIView.as_view(), name='consultant-experience-edit'),
    path('experiences/delete/<int:pk>/', ConsultantExperienceDetailAPIView.as_view(), name='consultant-experience-delete'),
    path('register/', RegisterAPIView.as_view(), name='register'),#para enviar email de registro exitoso
    path('validate/', ConsultantValidationView.as_view(), name='consultant-validation'),
    path('observation/', ObservationAPIView.as_view(), name='observation'),

]
