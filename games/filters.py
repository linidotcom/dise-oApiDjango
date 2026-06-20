import django_filters

from .models import Videojuego


class VideojuegoFilter(django_filters.FilterSet):
    estudio_nombre = django_filters.CharFilter(
        field_name="estudio__nombre", lookup_expr="icontains"
    )
    genero = django_filters.CharFilter(lookup_expr="icontains")
    anio_min = django_filters.NumberFilter(
        field_name="fecha_lanzamiento", lookup_expr="year__gte"
    )
    anio_max = django_filters.NumberFilter(
        field_name="fecha_lanzamiento", lookup_expr="year__lte"
    )
    precio_min = django_filters.NumberFilter(field_name="precio", lookup_expr="gte")
    precio_max = django_filters.NumberFilter(field_name="precio", lookup_expr="lte")

    class Meta:
        model = Videojuego
        fields = ["estudio", "plataforma", "genero", "estudio_nombre"]
