from rest_framework import serializers
from .models import Personas, Email, Telefono


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'

class TelefonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefono
        fields = '__all__'
class PersonaSerializer(serializers.ModelSerializer):
    telefonos = TelefonoSerializer(many=True, read_only=True)
    emails = EmailSerializer(many=True, read_only=True)
    class Meta:
        model = Personas
        fields = '__all__'