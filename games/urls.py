from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EstudioViewSet, VideojuegoViewSet

router = DefaultRouter()
router.register(r"estudios", EstudioViewSet, basename="estudio")
router.register(r"videojuegos", VideojuegoViewSet, basename="videojuego")

urlpatterns = [
    path("", include(router.urls)),
]
