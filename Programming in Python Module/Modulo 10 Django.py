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

    


"""
