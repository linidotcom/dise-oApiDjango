from django.contrib import admin

from .models import Estudio, Videojuego


@admin.register(Estudio)
class EstudioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "pais", "anio_fundacion")
    search_fields = ("nombre", "pais")


@admin.register(Videojuego)
class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "estudio", "plataforma", "precio", "calificacion")
    list_filter = ("plataforma", "estudio")
    search_fields = ("titulo", "genero")
