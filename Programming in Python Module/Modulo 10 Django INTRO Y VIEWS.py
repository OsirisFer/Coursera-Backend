"""
DJANGO PROJECT STRUCTURE
    MANAGE.PY
        Es el archivo principal, desde este se corren los comandos de Django: levantar el servidor, crear apps, migraciones
        Se puede usar django-admin como alternativa a manage.py
    SETTINGS.PY
        Archivo de configuración del proyecto Django. Se define la base de datos, las apps instaladas, middlewares, rutas estáticas, etc.
    URLS.PY
        Archivo donde se definen las rutas URL del proyecto. Se asignan vistas a URLs específicas
    WSGI.PY
        Archivo que sirve como punto de entrada para servidores web compatibles con WSGI para servir la aplicación Django.
    ASGI.PY
        Sirve para aplicaciones asíncronas y es el punto de entrada para servidores compatibles con ASGI.
    __init_.py ( NO SE TOCA )
        Indica que el directorio debe ser tratado como un paquete Python.

    App vs Project: 
        Una app es una funcionalidad específica dentro de un proyecto Django. 
        Un proyecto puede contener múltiples apps que trabajan juntas para formar una aplicación web completa.

    VENV: es un entorno virtual que aísla las dependencias de un proyecto Python
        python3 -m venv nombre_del_entorno   (para crear un entorno virtual)
        Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned  (para permitir la ejecución de scripts en PowerShell)
        .\nombre_del_entorno\Scripts\Activate  (para activar el entorno virtual en Windows PowerShell)
        pip3 install django  (para instalar Django dentro del entorno virtual)
        python3 -m django --version  (para verificar la instalación de Django)
        django-admin startproject nombre_del_proyecto  (para crear un nuevo proyecto Django)
        python3 manage.py runserver  (para iniciar el servidor de desarrollo de Django)
        django-admin startapp nombre_de_la_app  (para crear una nueva app dentro del proyecto)

        Si ya esta creado el entorno virtual y el proyecto:
        1) Primer paso ir al directorio del proyecto y activar el entorno virtual con .\tutorial-env\Scripts\Activate.ps1 
        2) Luego ir al directorio del proyecto (donde esta manage.py) y correr python3 manage.py runserver

DJANGO APP STRUCTURE
    MODELS.PY
        Archivo donde se definen las tablas de la base de datos. Cada modelo representa una tabla y sus atributos representan las columnas.
    VIEWS.PY
        Es la lógica de la aplicación. Es decir que mostraremos al usuario cuando visite una URL específica.
    URLS.PY
        Archivo donde se definen las rutas URL específicas para la app. Se asignan vistas a URLs dentro de la app.
    ADMIN.PY
        Archivo donde se registran los modelos para que sean gestionables desde el panel de administración de Django.
    APPS.PY
        Archivo que contiene la configuración de la app, como su nombre y otras opciones.
    TESTS.PY
        Archivo donde se escriben pruebas unitarias para la app.
    __init_.py ( NO SE TOCA )
        Indica que el directorio debe ser tratado como un paquete Python.
    MIGRATIONS/
        Guarda los cambiios de la base de datos cada vez que se crea o modifica un modelo. No se editan manualmente.

Las apps luego deben ser registradas en el archivo settings.py del proyecto para que Django las reconozca.
    EJ: INSTALL APPS = [
        'demoapp',  # Nombre de la app registrada
    ]

VIEW:
    La view es una función o clase en views.py que recibe una solicitud web y devuelve una respuesta web. Django por defecto crea un archivo views.py en el proyecto.
    En la app en el archivo views.py dentro de la app definimos una función que tome un objeto request como parámetro y retorne una respuesta HTTP:
        from django.http import HttpResponse
        def nombre_de_la_vista(request):
            return HttpResponse("Hola, esta es mi primera vista en Django!")
        
    luego creamos un archivo urls.py dentro de la app para definir la ruta URL que apunta a esa vista:
        from django.urls import path
        from . import views

        urlpatterns = [
            path('mi-vista/', views.nombre_de_la_vista, name='mi_vista'),
        ]
    luego en el archivo urls.py del proyecto incluimos las URLs de la app:
        
        from django.contrib import admin
        from django.urls import path, include
        from nombre_de_la_app import views

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('nombre_de_la_app.urls')
        ]
    Entonces basicamente lo que pasa es que el flujo es:
    El usuario llama a una URL -> el archivo urls.py del proyecto redirige a la urls.py de la app -> la urls.py de la app llama a la vista definida en views.py -> la vista procesa la solicitud y devuelve una respuesta HTTP al usuario.
    La funcion que creamos es llamada por el usuario cuando el usuario ingresa a la url que django matchea despues con esa función internamente, ese codigo no lo veo

    Basicamente la app funciona con request -> response
    HttpRequest es lo que el usuario manda, es decir una request que puede ser un get (pidiendo datos), post (enviando datos), put(request para actualizar) o delete(request de que se borre algo).
    A esa request se le devuelve un HttpResponse generalmente en forma de texto o html, es decir se le responde al usuario, enviando la respuesta al navegador

PARAMETERS
    Un parámetro es und ato que el cliente manda al servidor, existen 3 tipos
        1) Path parameters (en la URL)
        Django reconoce los parametros si estan entre <> son variables y se separan con /
        /getuser/John/1
        path('getuser/<name>/<id>', views.pathview)


        2) Query parameters (despues del ?)
            Ej: /getuser/?name=John&id=1
            Django no los define en urls.py, la vista los lee desde el request.get
            def qryview(request):
            name = request.GET['name']
            id = request.GET['id']
            return HttpResponse(f"Name:{name} UserID:{id}")

        3) Body parameters 
            No aparecen en la URL, viajan en el cuerpo del POST
            <form action="/myapp/getform/" method="POST">
                {% csrf_token %}
                <input type="text" name="id">
                <input type="text" name="name">
                <input type="submit">
            </form>

Path Converters (Tipo de dato) sirven para validar y convertir el valor
    <int:id> Django se asegura que sea un número si lo lo es da 404
    Otros: str, slug, uuid, path

NAMESPACES 
    En Django, cada URL puede tener un nombre y opcionalmente pertenecer a un namespace, que identifica 
    a qué aplicación pertenece esa URL y evita conflictos cuando varias apps tienen vistas con el mismo 
    nombre. En lugar de escribir URLs reales a mano, Django permite referirse a ellas por su nombre usando reverse()
    en las vistas o {% url %} en los templates, y automáticamente obtiene la ruta correcta. El namespace 
    (definido con app_name en urls.py) asegura que Django sepa exactamente qué URL usar, y reverse actúa como un 
    traductor que convierte el nombre de la URL en su path real, haciendo el código más claro, mantenible y seguro ante 
    cambios en las rutas.

ERRORES 
    Códigos comunes:
        200: correcto
        404: no encontrado
        403: prohibido
        400: solicitud inválida
        500: error interno

    HttpResponse → respuesta normal Si algo sale mal, se devuelve o se lanza un error.
    Django trae una clase específica para el error 404.
        
        HttpResponseNotFoun es como Http404, pero menos recomendado.
        from django.http import HttpResponseNotFound
        return HttpResponseNotFound("Page not found")
                
    Http404 → recurso no encontrado Es la forma recomendada, corta la ejecuciòn y muestra la pagina de error correspondiente
        from django.http import Http404
        raise Http404("Resource not found")

    PermissionDenied → Se lanza cuando el usuario no tiene permiso.
        from django.core.exceptions import PermissionDenied
        def myview(request):
            if not request.user.has_perm("app.view_model"):
                raise PermissionDenied
                
    Excepciones → forma correcta de manejar errores
    Usar excepciones, no if con textos de error
        from django.http import Http404
        def product_detail(request, id):
        if id != 1:
            raise Http404("Product not found")
        return HttpResponse("Product found")

    DEBUG=False → errores amigables en producción

"""
