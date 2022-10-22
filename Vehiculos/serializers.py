from pyexpat import model
from rest_framework import serializers
from .models import cliente,factura,vehiculos,categoria_vehiculos

from django.contrib.auth.models import User

from rest_framework import serializers
from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user  

class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model= cliente
        fields= ('__all__')

class facturaSerializer(serializers.ModelSerializer):
    class Meta:
        model= factura
        fields= ('__all__')
        read_only_fields=('fecha',)

class vehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model= vehiculos
        fields= ('__all__')

class categoria_vehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model= categoria_vehiculos
        fields= ('__all__')