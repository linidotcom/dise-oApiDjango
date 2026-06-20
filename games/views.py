from rest_framework import viewsets

from .filters import VideojuegoFilter
from .models import Estudio, Videojuego
from .serializers import EstudioSerializer, VideojuegoSerializer


class EstudioViewSet(viewsets.ModelViewSet):
    queryset = Estudio.objects.all()
    serializer_class = EstudioSerializer
    filterset_fields = ["pais", "anio_fundacion"]
    search_fields = ["nombre", "pais"]
    ordering_fields = ["nombre", "anio_fundacion"]


class VideojuegoViewSet(viewsets.ModelViewSet):
    queryset = Videojuego.objects.select_related("estudio").all()
    serializer_class = VideojuegoSerializer
    filterset_class = VideojuegoFilter
    search_fields = ["titulo", "genero", "estudio__nombre"]
    ordering_fields = ["titulo", "precio", "calificacion", "fecha_lanzamiento"]
