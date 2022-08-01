from rest_framework import serializers

from employees.models import Employee
from providers.serializers import ProviderSerializer

class EmployeeSerializer(serializers.ModelSerializer):
    provider = ProviderSerializer()
    
    class Meta:
        model = Employee
        fields = (
            'email', 
            'username', 
            'birthday',
            'gender',
            'provider'
            'last_visit'
        )
    

class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'email', 
            'username', 
            'birthday',
            'provider'
            'password'
        )
        
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return Employee.objects.create_user(**validated_data)
