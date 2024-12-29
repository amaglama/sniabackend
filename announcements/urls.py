from django.urls import path
from .views import AnnouncementCreateAPIView, AnnouncementUpdateAPIView, Getbyid, Delete, FilterByModuleandType,  ModuleList, TypeList, Download


urlpatterns = [
    path('announcements/create', AnnouncementCreateAPIView.as_view(), name='announcement-list-create'),
    path('announcements/list/<int:pk>', Getbyid.as_view(), name='listbyid'),
    path('announcements/delete/<int:pk>', Delete.as_view(), name='delete'),
    path('announcements/edit/<int:pk>', AnnouncementUpdateAPIView.as_view(), name='announcement-edit'),
    path('announcements/filter/<int:id_module>/<int:id_type>',FilterByModuleandType.as_view(), name='filter'),
    path('announcements/moduleList', ModuleList.as_view(), name='module-list'),
    path('announcements/typeList', TypeList.as_view(), name='type-list'),
    path('announcements/download/<str:document_name>', Download.as_view(), name='download_document'),
]