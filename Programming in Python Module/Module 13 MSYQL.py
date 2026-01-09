"""

    Django es independiente del motor de base de datos:
        el ORM funciona igual sin importar si se usa SQLite, MySQL o PostgreSQL.

MYSQL EN DJANGO
    Para usar MySQL es necesario:
        - crear la base de datos manualmente
        - instalar un driver (mysqlclient)
        - configurar la conexión en settings.py

    Datos necesarios para la conexión:
        - nombre de la base
        - usuario
        - contraseña
        - host
        - puerto

    Django usa un driver para:
        - traducir queries del ORM a SQL específico de MySQL
        - mapear modelos a tablas

    La conexión a la base de datos se maneja por request
    y se controla con:
        CONN_MAX_AGE   # tiempo que la conexión permanece abierta

SEGURIDAD DE CREDENCIALES
    Las credenciales de la base de datos:
        - NO deben estar dentro del proyecto
        - pueden almacenarse en un archivo externo (ej: etc/mysql)
        - esto es una medida de seguridad deliberada

    El archivo externo contiene:
        - usuario
        - contraseña
        - nombre de la base

    Es responsabilidad del desarrollador:
        - proteger las credenciales
        - usar contraseñas seguras
        - asignar permisos correctos en la base
        - proteger datos sensibles de los usuarios

MYSQL – CONFIGURACIÓN TÉCNICA EN DJANGO (DETALLE PRÁCTICO)
    Para usar MySQL con Django es necesario:
        - instalar el servidor MySQL
        - crear la base de datos manualmente (Django no la crea)
        - instalar un driver DB-API compatible (mysqlclient)

    Instalación del driver recomendado por Django:
        pip install mysqlclient

    Creación manual de la base de datos:
        mysql -u root -p
        CREATE DATABASE mydatabase;

CONFIGURACIÓN EN settings.py
    La base de datos debe llamarse 'default':
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'mydatabase',
                'USER': 'root',
                'PASSWORD': 'password',
                'HOST': '127.0.0.1',
                'PORT': '3306',
                'OPTIONS': {
                    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
                }
            }
        }

    STRICT_TRANS_TABLES:
        - evita guardar datos inválidos
        - fuerza validaciones más estrictas
        - recomendado en producción

    Otras opciones avanzadas posibles:
        - default-character-set (utf8)
        - read_default_file (archivo externo de configuración)
        - init_command (comandos al conectarse)

CREACIÓN DE TABLAS EN MYSQL
    Django NO crea la base de datos, pero sí las tablas.
    Para generar las tablas:
        python manage.py migrate

    Esto crea automáticamente:
        - tablas de admin
        - auth
        - sessions
        - contenttypes
        - tablas de tus apps

VISUALIZACIÓN DE MYSQL EN VS CODE
    Se puede administrar MySQL desde VS Code usando una extensión.
    Permite:
        - ver bases de datos
        - ver tablas
        - inspeccionar datos
        sin usar la terminal de MySQL

ERROR COMÚN DE AUTENTICACIÓN MYSQL
    Error:
        Client does not support authentication protocol requested by server

    Solución:
        ALTER USER 'root'@'localhost'
        IDENTIFIED WITH mysql_native_password BY 'password';

        FLUSH PRIVILEGES;

MYSQL – CONFIGURACIÓN EN DJANGO (WINDOWS)
    En Windows, MySQL se instala mediante el instalador oficial
    (MySQL Installer Community).

    Durante la instalación se define:
        - contraseña del usuario root
        - puerto (por defecto 3306)
        - método de autenticación

ACCESO A MYSQL EN WINDOWS
    Abrir "MySQL Command Line Client" o CMD y ejecutar:
        mysql -u root -p

    Crear base de datos:
        CREATE DATABASE feedback;

    Crear usuario específico para Django (no usar root):
        CREATE USER 'admindjango'@'localhost'
        IDENTIFIED BY 'password';

    Asignar permisos al usuario:
        GRANT ALL PRIVILEGES ON feedback.*
        TO 'admindjango'@'localhost';

    Aplicar cambios:
        FLUSH PRIVILEGES;

INSTALACIÓN DEL DRIVER MYSQL PARA DJANGO
    En el entorno virtual del proyecto:
        pip install mysqlclient

    (En Windows puede requerir:
        - Microsoft C++ Build Tools
        - o usar una wheel precompilada)

CONFIGURACIÓN EN DJANGO (settings.py)
    Archivo:
        myproject/settings.py

    Configuración DATABASES:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'feedback',
                'USER': 'admindjango',
                'PASSWORD': 'password',
                'HOST': '127.0.0.1',
                'PORT': '3306',
                'OPTIONS': {
                    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                }
            }
        }

    STRICT_TRANS_TABLES:
        - evita datos inválidos
        - obliga validaciones estrictas
        - recomendado en producción

CREACIÓN DE TABLAS DESDE DJANGO
    Django NO crea la base de datos,
    pero sí crea las tablas a partir de los modelos.

    Comandos:
        python manage.py makemigrations
        python manage.py migrate

    Esto crea tablas para:
        - apps propias
        - admin
        - auth
        - sessions
        - contenttypes

"""