from django.db import models


class Estudio(models.Model):
    """Estudio desarrollador de videojuegos."""
    nombre = models.CharField(max_length=150, unique=True)
    pais = models.CharField(max_length=80)
    anio_fundacion = models.PositiveIntegerField()
    sitio_web = models.URLField(blank=True)

    class Meta:
        verbose_name = "Estudio"
        verbose_name_plural = "Estudios"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Videojuego(models.Model):
    """Videojuego. Pertenece a un Estudio (relacion 1:N via ForeignKey)."""

    class Plataforma(models.TextChoices):
        PC = "PC", "PC"
        PS5 = "PS5", "PlayStation 5"
        XBOX = "XBOX", "Xbox Series"
        SWITCH = "SWITCH", "Nintendo Switch"
        MOBILE = "MOBILE", "Movil"

    titulo = models.CharField(max_length=200)
    estudio = models.ForeignKey(
        Estudio,
        on_delete=models.CASCADE,
        related_name="videojuegos",
    )
    genero = models.CharField(max_length=80)
    plataforma = models.CharField(
        max_length=10,
        choices=Plataforma.choices,
        default=Plataforma.PC,
    )
    fecha_lanzamiento = models.DateField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    calificacion = models.FloatField(default=0)
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Videojuego"
        verbose_name_plural = "Videojuegos"
        ordering = ["-fecha_lanzamiento"]

    def __str__(self):
        return f"{self.titulo} ({self.estudio.nombre})"
