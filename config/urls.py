from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # API REST
    path("api/", include("games.urls")),

    # Esquema OpenAPI (JSON)
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Documentacion interactiva Swagger UI
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    # Documentacion alternativa ReDoc
    path(
        "redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
