from django.urls import path
from .views import (
    ConsultantRencaListCreateAPIView, ConsultantRencaRetrieveUpdateDestroyAPIView,
    ConsultantExperienceRencaRetrieveAPIView,RetrieveDepositRencaView,
    ConsultantExperienceRencaListCreateAPIView, BulkCreateDepositRencaView, EditDepositRencaView, DeleteDepositRencaView, ListDepositsRencaView, 
)
from .views import ConsultantExperienceRencaListCreateAPIView, ConsultantExperienceRencaDetailAPIView

urlpatterns = [
    path('consultants/renca/', ConsultantRencaListCreateAPIView.as_view(), name='consultant-list-create'),
    path('consultants/renca/<int:pk>/', ConsultantRencaRetrieveUpdateDestroyAPIView.as_view(), name='consultant-detail'),
    path('deposits/renca/', ListDepositsRencaView.as_view(), name='deposits_renca_list'),
    path('deposits/renca/<int:pk>/', RetrieveDepositRencaView.as_view(), name='deposit_renca_detail'),
    path('deposits/renca/bulk/create/', BulkCreateDepositRencaView.as_view(), name='deposits_renca_bulk_create'),
    path('deposits/renca/edit/<int:pk>/', EditDepositRencaView.as_view(), name='deposit_renca_edit'),
    path('deposits/renca/delete/<int:pk>/', DeleteDepositRencaView.as_view(), name='deposit_renca_delete'),
    path('experiences/renca/', ConsultantExperienceRencaListCreateAPIView.as_view(), name='experience_renca_-list'),
    path('experiences/renca/<int:pk>/', ConsultantExperienceRencaRetrieveAPIView.as_view(), name='consultant-experience-renca-detail'),
    path('experiences/renca/bulk/create/', ConsultantExperienceRencaListCreateAPIView.as_view(), name='experiences-renca-bulk-list-create'),
    path('experiences/renca/edit/<int:pk>/', ConsultantExperienceRencaDetailAPIView.as_view(), name='consultant-experience-renca-edit'),
    path('experiences/renca/delete/<int:pk>/', ConsultantExperienceRencaDetailAPIView.as_view(), name='consultant-experience-renca-delete'),
   
]
