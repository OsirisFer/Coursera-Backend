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

DTL – DJANGO TEMPLATE LANGUAGE
    Lenguaje de templates de Django para generar HTML dinámico.
    Inspirado en Jinja2.
    Aplica DRY (Do Not Repeat Yourself).
    El template NO ejecuta Python → más seguridad.

TEMPLATE ENGINE (idea clave)
    Combina:
        - HTML estático
        - placeholders DTL
        - datos del contexto (dict)
    Produce HTML final para el navegador.

CONSTRUCTOS BÁSICOS (4)
    Variables
    Tags
    Filters
    Comments

VARIABLES
    Muestran datos enviados desde la vista (context dictionary).

    Sintaxis:
        {{ variable }}

    Acceso con notación de punto:
        Diccionarios:
            {{ person.name }}
        Atributos:
            {{ user.username }}
        Listas:
            {{ items.0 }}

TAGS
    Agregan lógica de presentación (no lógica de negocio).
    Sintaxis general:
        {% tag %}

    Condicional:
        {% if user.is_authenticated %}
            ...
        {% else %}
            ...
        {% endif %}

    Iteración:
        {% for item in items %}
            {{ item.name }}
        {% endfor %}

    FOR – variables útiles:
        forloop.counter       → contador desde 1
        forloop.revcounter    → contador desde el final
        forloop.first         → True si es el primero
        forloop.last          → True si es el último
        forloop.parentloop    → loop externo en loops anidados

    Otros tags importantes:
        {% csrf_token %}      → protección en formularios POST
        {% include "file.html" %} → incluir otro template
        {% with var=value %}  → variable temporal
        {% block name %}      → herencia de templates

FILTERS
    Modifican SOLO la salida renderizada.
    Sintaxis:
        {{ variable | filter }}

    Filtros comunes:
        {{ name | upper }}
        {{ text | title }}
        {{ items | length }}
        {{ date | date:"Y-m-d" }}

    Filtros útiles:
        {{ value | default:"none" }}
        {{ words | join:"_" }}
        {{ list | first }}
        {{ list | last }}
        {{ text | wordcount }}

COMMENTS
    Comentarios internos del template.
    No se renderizan.

    Inline:
        {# comentario #}

    Bloque:
        {% comment %}
            contenido ignorado
        {% endcomment %}

FLUJO COMPLETO: MODELO → VISTA → TEMPLATE
    Django permite mostrar datos dinámicos desde la base de datos
    con muy pocos pasos y sin escribir SQL.

PASO 1 – MODELO (models.py)
    Se define el modelo que representa los datos en la base.

    Ejemplo:
        class Menu(models.Model):
            name = models.CharField(max_length=100)
            price = models.IntegerField()

            def __str__(self):
                return self.name

    El __str__ sirve para:
        - Admin de Django
        - Identificación visual de objetos

PASO 2 – DATOS EN LA BASE
    Los datos se cargan desde Django Admin:
        hummus, falafel, baklava, etc.

    No se escriben en código.

PASO 3 – CONSULTA ORM (views.py)
    La vista obtiene los datos desde el modelo usando el ORM.

    Ejemplo:
        from .models import Menu

        def menu(request):
            menu_items = Menu.objects.all()
            context = {'menu': menu_items}
            return render(request, 'menu_card.html', context)

    Menu.objects.all():
        - Devuelve un QuerySet
        - Contiene todos los registros de la tabla

PASO 4 – URL CONFIGURATION (urls.py)
    Se conecta la vista con una URL.

    Ejemplo:
        path('menu_cards/', views.menu, name='menu')

PASO 5 – TEMPLATE (menu_card.html)
    El template recibe el QuerySet y lo renderiza.
    No conoce la base de datos.

    Validación del contenido:
        {% if menu %}

    Iteración con for:
        {% for item in menu %}
            <p>{{ item.name }} - {{ item.price }}</p>
        {% endfor %}

    Manejo de lista vacía:
        {% else %}
            <p>No items available</p>
        {% endif %}

PASO 6 – RENDER FINAL
    Django:
        - Ejecuta la vista
        - Obtiene los datos del modelo
        - Pasa el contexto al template
        - Renderiza HTML al navegador

ACTUALIZACIÓN AUTOMÁTICA
    Al agregar un nuevo item en Django Admin:
        - No se cambia código
        - Solo se refresca la página
        - El nuevo dato aparece automáticamente

DIFERENCIA CLAVE CON EJEMPLOS ANTERIORES
    Antes:
        Diccionarios hardcodeados en la vista
    Ahora:
        Datos reales desde la base de datos

IDEA CENTRAL
    El modelo maneja datos
    La vista prepara datos
    El template solo los muestra

BASE TEMPLATE (base.html)
    Contiene la estructura general del sitio.
    NO se renderiza directamente.

    Usa bloques vacíos que los hijos pueden sobrescribir.

    Ejemplo:
        <!-- contenido principal -->
        {% block contents %}
        {% endblock %}

DEFINICIÓN DE BLOQUES
    Los bloques se declaran con:
        {% block nombre %}
        {% endblock %}

    El nombre identifica qué parte puede ser sobrescrita.

EJEMPLO DE BASE.HTML (estructura)
    - Header fijo
    - Sidebar fija
    - Content dinámico (block)
    - Footer fijo o extendible

CHILD TEMPLATE (home.html, register.html, login.html)
    Heredan la base usando:
        {% extends "base.html" %}

    Solo definen los bloques necesarios.

    Ejemplo:
        {% block contents %}
            <h2>This is Home page</h2>
        {% endblock %}

SOBRESCRIBIR BLOQUES
    El contenido del bloque en el hijo
    reemplaza el bloque del padre.

MÚLTIPLES BLOQUES
    Un template puede tener varios bloques:
        - contents
        - footer
        - header

    Cada hijo decide cuáles sobrescribir.

USO DE {{ block.super }}
    Permite reutilizar el contenido del bloque padre
    y agregar más contenido.

    Ejemplo en login.html:
        {% block footer %}
            {{ block.super }}
            <h4>Designed By: Alexa Designs Ltd</h4>
        {% endblock %}

    Similar a super() en Python.

VIEWS ASOCIADAS
    Cada página tiene su vista,
    pero todas comparten el mismo layout.

    Ejemplo:
        def home(request):
            return render(request, "home.html", {})

        def register(request):
            return render(request, "register.html", {})

        def login(request):
            return render(request, "login.html", {})

STATIC FILES (ARCHIVOS ESTÁTICOS)
    Contienen:
        - CSS
        - JS
        - imágenes

CONFIGURACIÓN
    django.contrib.staticfiles debe estar en INSTALLED_APPS
    STATIC_URL = 'static/'

UBICACIÓN RECOMENDADA
    myapp/static/myapp/

USO EN TEMPLATES
    Primero cargar static:
        {% load static %}

    Luego referenciar el archivo:
        <img src="{% static 'myapp/example.jpg' %}">

IDEA CENTRAL
    base.html define la estructura
    child templates definen el contenido
    static sirve archivos no dinámicos
    
EXTENDS vs INCLUDE (DTL)

OBJETIVO
    Reutilizar estructura y componentes comunes
    sin duplicar código en múltiples páginas.

EXTENDS
    Crea relación padre → hijo entre templates.
    El template hijo HEREDA la estructura del padre
    y SOLO reemplaza bloques definidos.

    Se usa para:
        - layout general
        - estructura principal
        - estilos comunes

    Sintaxis:
        {% extends "base.html" %}

    Reemplazo de contenido:
        {% block content %}
            contenido propio de la página
        {% endblock %}

INCLUDE
    Inserta un template dentro de otro.
    NO hereda estructura.
    Solo “pega” el contenido renderizado.

    Se usa para:
        - headers
        - footers
        - navbars
        - componentes reutilizables

    Sintaxis:
        {% include "partials/_header.html" %}

DIFERENCIA CLAVE
    extends → herencia (estructura completa)
    include → composición (fragmentos)

ESTRUCTURA DE ARCHIVOS RECOMENDADA
    templates/
        base.html
        home.html
        about.html
        menu.html
        partials/
            _header.html

BASE TEMPLATE (base.html)
    Contiene:
        - HTML base
        - estilos globales
        - bloques reutilizables
        - includes comunes

    Ejemplo:
        <main>
            {% include "partials/_header.html" %}
            {% block content %}{% endblock %}
        </main>

CHILD TEMPLATES
    Heredan base.html
    Definen solo su contenido único

    Ejemplo:
        {% extends "base.html" %}
        {% block content %}
            <p>Contenido de la página</p>
        {% endblock %}

FLUJO FINAL
    View → render(child.html)
        → child extiende base
        → base incluye parciales
        → bloques se reemplazan

VENTAJA PRINCIPAL
    Un solo cambio en base o partial
    afecta automáticamente a todo el sitio

"""