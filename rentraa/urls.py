from django.urls import path
from . import views
from .views import RegistroCreateAPIView, RetrieveRecord, DeleteRecord


urlpatterns = [
    path('rentraa/asd/', views.hello_world, name='hello_world'),
    path('rentraa/list', RegistroCreateAPIView.as_view(), name='consultant-list-create'),
    path('rentraa/list/<int:pk>', RetrieveRecord.as_view(), name='list'),
    path('rentraa/delete/<int:pk>/', DeleteRecord.as_view(), name='deposit_delete'),

]
