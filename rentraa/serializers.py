from rest_framework import serializers
from .models import Rentraa


#class RentraaSerializer(serializers.Serializer):
#    name = serializers.CharField()
#    lastname = serializers.CharField()
#    is_deleted = serializers.BooleanField()


class RentraaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rentraa
        fields = '__all__'


