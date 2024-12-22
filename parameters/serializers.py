from rest_framework import serializers
from .models import State, BankAccount, Category, Province, Municipality 

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'  

class ProvinceSerializer(serializers.ModelSerializer):
    state = StateSerializer(read_only=True)  # Relación con State

    class Meta:
        model = Province
        fields = '__all__'


class MunicipalitySerializer(serializers.ModelSerializer):
    province = ProvinceSerializer(read_only=True)  # Relación con Province

    class Meta:
        model = Municipality
        fields = '__all__'    

class MunicipalityReverseSerializer(serializers.ModelSerializer):
    province = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()

    class Meta:
        model = Municipality
        fields = ['id', 'municipality_code', 'ulot_name', 'province', 'state']

    def get_province(self, obj):
        return ProvinceSerializer(obj.province).data

    def get_state(self, obj):
        return StateSerializer(obj.province.state).data
class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =  ['id', 'name', 'registration_fee', 'renewal_fee', 'description', 'abbreviation', 'type']


#para los combos

class StateCascadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'name']


class ProvinceCascadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['id', 'province_name']


class MunicipalityCascadeSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()  # Campo dinámico

    class Meta:
        model = Municipality
        fields = ['id', 'ine_name', 'ulot_name','mepf_name','name']

    def get_name(self, obj):
        # Decidir dinámicamente el nombre que se devuelve
        request = self.context.get('request', None)
        filter_name = request.query_params.get('filter_name', 'ine_name') if request else 'ine_name'
        return getattr(obj, filter_name, obj.ine_name)  # Por defecto: ine_name
        
