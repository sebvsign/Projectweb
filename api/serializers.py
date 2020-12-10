from rest_framework import serializers
from equipos.models import Equipo


class EquiposListaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'