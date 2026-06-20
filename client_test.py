"""
Cliente de prueba de la API Tienda de Videojuegos.
Ejecuta:  python client_test.py
(con el servidor corriendo en http://127.0.0.1:8000)

Hace un POST (crear) y varios GET (listar y filtrar) e imprime los resultados.
"""
import requests

BASE = "http://127.0.0.1:8000/api"


def imprimir(titulo, respuesta):
    print("\n" + "=" * 60)
    print(titulo, "->", respuesta.status_code)
    print("=" * 60)
    try:
        print(respuesta.json())
    except Exception:
        print(respuesta.text)


def main():
    # 1) POST: crear un estudio
    estudio = {
        "nombre": "Estudio Demo",
        "pais": "Mexico",
        "anio_fundacion": 2015,
        "sitio_web": "https://demo.example.com",
    }
    r = requests.post(f"{BASE}/estudios/", json=estudio)
    imprimir("POST /estudios/ (crear estudio)", r)
    estudio_id = r.json().get("id")

    # 2) POST: crear un videojuego ligado a ese estudio
    juego = {
        "titulo": "Aventura Pixelada",
        "estudio": estudio_id,
        "genero": "Aventura",
        "plataforma": "PC",
        "fecha_lanzamiento": "2023-05-10",
        "precio": "499.99",
        "calificacion": 8.7,
        "stock": 25,
    }
    r = requests.post(f"{BASE}/videojuegos/", json=juego)
    imprimir("POST /videojuegos/ (crear videojuego)", r)

    # 3) GET: listar todos los videojuegos
    r = requests.get(f"{BASE}/videojuegos/")
    imprimir("GET /videojuegos/ (listar)", r)

    # 4) GET con filtro: por nombre de estudio
    r = requests.get(f"{BASE}/videojuegos/", params={"estudio_nombre": "Demo"})
    imprimir("GET /videojuegos/?estudio_nombre=Demo (filtrar)", r)


if __name__ == "__main__":
    main()
