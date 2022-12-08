from rest_framework import serializers

# modelos a serializar
from .models import Usuarios
from .models import Carreras


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'  

class CarrerasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carreras
        fields = '__all__'  





         

             
