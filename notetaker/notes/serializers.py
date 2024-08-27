from rest_framework import serializers
from .models import Nota

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = '__all__'

    def validate_titulo(self, value):
        if len(value) > 10:
            raise serializers.ValidationError("El título no debe tener mas de 10 caracteres.")
        return value

    def validate_contenido(self, value):
        if len(value) < 5 or len(value) > 100:
            raise serializers.ValidationError("El contenido debe tener entre 5 y 100 caracteres.")
        return value
