from django.urls import path
from .views import AnnouncementCreateAPIView, AnnouncementUpdateAPIView, Getbyid, Delete, FilterByModuleandType


urlpatterns = [
    path('announcements/create', AnnouncementCreateAPIView.as_view(), name='announcement-list-create'),
    path('announcements/list/<int:pk>', Getbyid.as_view(), name='listbyid'),
    path('announcements/delete/<int:pk>', Delete.as_view(), name='delete'),
    path('announcements/edit/<int:pk>', AnnouncementUpdateAPIView.as_view(), name='announcement-edit'),
    path('announcements/filter/<str:module>/<str:type>',FilterByModuleandType.as_view(), name='filter'),
]
