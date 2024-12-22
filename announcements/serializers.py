from rest_framework import serializers
from .models import Announcement

class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'