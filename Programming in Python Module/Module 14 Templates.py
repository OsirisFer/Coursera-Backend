"""
TEMPLATES EN DJANGO (DTL)
    Los templates son documentos de texto (HTML) que usan
    el Django Template Language (DTL) para insertar contenido dinámico.

CONTENIDO DINÁMICO EN TEMPLATES
    Las variables dinámicas se insertan usando:
        {{ variable }}
    Estas variables vienen del contexto enviado por la vista
    a través de la función render().

    Ejemplo conceptual:
        render(request, "template.html", {
            "dish_name": "Pizza",
            "price": 500
        })

DJANGO TEMPLATE ENGINE
    Django usa un Template Engine para:
        - interpretar el DTL
        - combinar HTML estático + datos dinámicos
        - generar HTML final para el navegador

    El DTL incluye:
        - variables: {{ }}
        - tags: {% %}
        - filters
        - comments

CONFIGURACIÓN DE TEMPLATES (settings.py)
    La configuración del motor de templates se define en:
        settings.py

    Parámetros importantes:
        - APP_DIRS = True
            Permite buscar templates dentro de cada app
            en carpetas llamadas "templates"

        - DIRS
            Permite agregar rutas custom donde Django
            buscará templates globales

MÚLTIPLES TEMPLATE ENGINES
    Django permite usar más de un template engine.
    Ejemplo:
        - Django Templates (DTL)
        - Jinja2

    Se configuran también en settings.py.

REUTILIZACIÓN DE CÓDIGO – TEMPLATE INHERITANCE
    Django soporta herencia de templates para reutilizar HTML.

    Se define un template base con bloques:
        {% block content %}{% endblock %}

    Los templates hijos:
        - heredan el base template
        - sobreescriben solo los bloques necesarios

    Beneficios:
        - evita duplicar HTML
        - facilita mantenimiento
        - aplica principio DRY (Don't Repeat Yourself)

BUENA PRÁCTICA
    Colocar los templates dentro de una carpeta:
        templates/
    ya sea:
        - dentro de cada app
        - o como carpeta global configurada en DIRS

FLUJO COMPLETO PARA CREAR Y RENDERIZAR UN TEMPLATE (CON CÓDIGO)

1. Crear una vista que use render()
    Archivo: myapp/views.py

    from django.shortcuts import render

    def about(request):
        return render(request, "about.html", {})

2. Configurar URLs de la app
    Archivo: myapp/urls.py

    from django.urls import path
    from . import views

    urlpatterns = [
        path("about/", views.about, name="about"),
    ]

3. Incluir URLs de la app en el proyecto
    Archivo: myproject/urls.py

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("", include("myapp.urls")),
    ]

4. Configurar settings.py (templates y app)
    Archivo: myproject/settings.py

    INSTALLED_APPS = [
        ...
        "myapp",
    ]

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [BASE_DIR / "templates"],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

5. Crear carpeta y archivo del template
    Estructura:
        project/
        ├── templates/
        │   └── about.html

6. Crear HTML estático
    Archivo: templates/about.html

    <!DOCTYPE html>
    <html>
    <head>
        <title>About</title>
    </head>
    <body>
        <h2>About</h2>
    </body>
    </html>

7. Crear contenido dinámico en la vista
    Archivo: myapp/views.py

    from django.shortcuts import render

    def about(request):
        about_content = {
            "about": "Little Lemon is a family-owned restaurant."
        }
        return render(request, "about.html", about_content)

8. Usar variables del contexto en el template
    Archivo: templates/about.html

    <!DOCTYPE html>
    <html>
    <head>
        <title>About</title>
    </head>
    <body>
        <h2>About</h2>
        <p>{{ about }}</p>
    </body>
    </html>

DINAMISMO REAL DEL TEMPLATE
    Si se modifica el diccionario en la vista:
        about_content["about"] = "Nuevo texto"

    No es necesario tocar el HTML.
    Al refrescar la página, el contenido se actualiza.

SEPARACIÓN DE RESPONSABILIDADES
    - views.py:
        obtiene datos (diccionario, BD, lógica)
    - template (.html):
        muestra datos (HTML + DTL)
    - urls.py:
        conecta URL con la vista
    - settings.py:
        define dónde buscar templates



"""