from rest_framework import serializers
from .models import Announcement, AnnouncementType, AnnouncementModule

class SerializerAnnouncement(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'


class SerializerAnnouncementType(serializers.ModelSerializer):
    class Meta:
        model = AnnouncementType
        fields = '__all__'


class SerializerAnnouncementModule(serializers.ModelSerializer):
    class Meta:
        model = AnnouncementModule
        fields = '__all__'