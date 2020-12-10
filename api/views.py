from rest_framework import viewsets, permissions 
from .serializers  import EquiposListaSerializer
from equipos.models import Equipo

# Create your views here.

class EquiposListaJson(viewsets.ModelViewSet):
    """
    API endpoint que lista los equipos creados.
    """

    queryset = Equipo.objects.all().order_by('titulo')
    serializer_class = EquiposListaSerializer