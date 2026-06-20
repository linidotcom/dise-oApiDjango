from rest_framework import serializers

from .models import Estudio, Videojuego


class EstudioSerializer(serializers.ModelSerializer):
    total_videojuegos = serializers.IntegerField(
        source="videojuegos.count", read_only=True
    )

    class Meta:
        model = Estudio
        fields = [
            "id",
            "nombre",
            "pais",
            "anio_fundacion",
            "sitio_web",
            "total_videojuegos",
        ]


class VideojuegoSerializer(serializers.ModelSerializer):
    estudio_nombre = serializers.CharField(source="estudio.nombre", read_only=True)

    class Meta:
        model = Videojuego
        fields = [
            "id",
            "titulo",
            "estudio",
            "estudio_nombre",
            "genero",
            "plataforma",
            "fecha_lanzamiento",
            "precio",
            "calificacion",
            "stock",
        ]

    def validate_calificacion(self, value):
        if not (0 <= value <= 10):
            raise serializers.ValidationError("La calificacion debe estar entre 0 y 10.")
        return value
