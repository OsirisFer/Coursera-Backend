"""
DJANGO ADMIN – GESTIÓN DE USUARIOS Y MODELOS

Admin y autenticación:
    Django incluye un sistema de autenticación y autorización listo para usar
    a través de django.contrib.admin, que viene instalado por defecto.
    Corro el servidor y agrego /admin a la URL

    Se puede ver en settings.py:
        INSTALLED_APPS incluye django.contrib.admin, auth, etc.

SUPERUSER:
    El superuser tiene permisos completos:
        - crear y modificar usuarios
        - crear y modificar grupos
        - asignar permisos
        - administrar todos los modelos

    Solo los usuarios con:
        is_staff = True
    pueden ingresar al panel de administración.

USUARIOS Y PERMISOS:
    Un usuario sin permisos no puede hacer nada útil.
    Los permisos se pueden asignar:
        - individualmente
        - mediante grupos (recomendado)

    Los grupos permiten manejar permisos comunes para varios usuarios.

RIESGOS DEL ADMIN POR DEFECTO:
    Un usuario staff:
        - puede modificar otros usuarios
        - puede cambiar sus propios permisos
        - puede asignarse privilegios de superuser

    Django Admin por defecto NO restringe estas acciones.

CUSTOMIZAR USER ADMIN

Paso 1: Desregistrar el UserAdmin por defecto (admin.py)

    from django.contrib import admin
    from django.contrib.auth.models import User

    admin.site.unregister(User)

Paso 2: Registrar un UserAdmin personalizado

    from django.contrib.auth.admin import UserAdmin

    @admin.register(User)
    class NewAdmin(UserAdmin):
        pass

    Al inicio, no hay cambios visibles en la interfaz.

CAMPOS SOLO LECTURA (readonly_fields):
    Permite evitar que ciertos campos sean modificados.

Ej:
    Evitar que se modifique date_joined:

    @admin.register(User)
    class NewAdmin(UserAdmin):
        readonly_fields = ['date_joined']

    El campo aparece deshabilitado en el admin.

RESTRICCIÓN SEGÚN EL USUARIO (get_form):
    Se puede permitir que solo el superuser modifique ciertos campos.

Ej:
    Evitar que usuarios staff modifiquen el username:

    @admin.register(User)
    class NewAdmin(UserAdmin):
        def get_form(self, request, obj=None, **kwargs):
            form = super().get_form(request, obj, **kwargs)
            if not request.user.is_superuser:
                form.base_fields['username'].disabled = True
            return form

    Resultado:
        - Solo el superuser puede cambiar usernames
        - Staff no puede romper cuentas ajenas

ADMINISTRAR MODELOS DE LA APP

Paso 1: Crear la app y registrarla

    Agregar la app en INSTALLED_APPS:
        'myapp.apps.MyappConfig'

Paso 2: Crear un modelo (models.py)

    from django.db import models

    class Person(models.Model):
        last_name = models.TextField()
        first_name = models.TextField()

Paso 3: Registrar el modelo en admin.py

    from django.contrib import admin
    from .models import Person

    admin.site.register(Person)

    El modelo aparece automáticamente en el admin.

__str__ (representación legible):
    Sirve para mostrar un texto más descriptivo en el admin.

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

CUSTOMIZAR LA VISTA DEL MODELO EN ADMIN

Usar ModelAdmin:

    @admin.register(Person)
    class PersonAdmin(admin.ModelAdmin):
        list_display = ("last_name", "first_name")

    Resultado:
        - columnas separadas
        - campos clickeables para editar

Agregar búsqueda:

    class PersonAdmin(admin.ModelAdmin):
        list_display = ("last_name", "first_name")
        search_fields = ("first_name__startswith", )

    Permite filtrar resultados desde el admin.

Resumen:
    - Django Admin permite gestionar usuarios, grupos y modelos
    - is_staff controla acceso al admin
    - Los permisos deben asignarse cuidadosamente
    - UserAdmin se puede personalizar para mayor seguridad
    - ModelAdmin permite personalizar cómo se muestran los modelos
    - __str__, list_display y search_fields mejoran la usabilidad

SISTEMA BÁSICO DE RESERVAS CON DJANGO ADMIN

Objetivo:
    Crear un sistema simple de reservas usando Django Admin,
    permitiendo a los empleados registrar y gestionar reservas
    sin escribir interfaces personalizadas.

MODELO DE RESERVA (models.py):
    El modelo Reservation contiene los datos de la reserva:
        - nombre del cliente
        - contacto
        - hora de llegada
        - cantidad de personas
        - notas adicionales

    class Reservation(models.Model):
        name = models.CharField(max_length=200)
        contact = models.CharField(max_length=50)
        time = models.TimeField()
        guests = models.IntegerField()
        notes = models.TextField()

Agregar representación legible:
    Se usa __str__ para mostrar información útil en el admin.

    def __str__(self):
        return self.name

CONFIGURACIÓN INICIAL:
    - Agregar la app en INSTALLED_APPS (settings.py)
    - Crear migraciones:
        python manage.py makemigrations
        python manage.py migrate

CREAR SUPERUSER:
    Se necesita un superusuario para acceder al admin.

        python manage.py createsuperuser

    El superuser puede:
        - administrar modelos
        - crear usuarios
        - crear grupos
        - asignar permisos

REGISTRAR EL MODELO EN ADMIN (admin.py):
    from django.contrib import admin
    from .models import Reservation

    admin.site.register(Reservation)

    Esto hace que el modelo aparezca en Django Admin.

USAR DJANGO ADMIN:
    Acceso:
        http://localhost:8000/admin

    Funcionalidades:
        - agregar reservas
        - editar reservas
        - eliminar reservas
        - ver historial de cambios

    El formulario se genera automáticamente a partir del modelo.

GESTIÓN DE USUARIOS:
    Desde Admin se pueden:
        - crear usuarios
        - asignar contraseñas seguras
        - definir datos personales
        - asignar permisos

    Permisos importantes:
        is_staff:
            permite acceder al admin
        is_superuser:
            acceso total

    Se pueden asignar permisos específicos:
        - ver
        - agregar
        - cambiar
        - eliminar registros

FILTROS Y VISTAS:
    - Se pueden filtrar usuarios por superuser
    - Se pueden ver fechas importantes:
        last_login
        date_joined

GRUPOS:
    Se pueden crear grupos para:
        - agrupar permisos
        - asignar roles (ej: staff)

    Ej:
        Grupo "staff" con permisos para gestionar reservas.

BASE DE DATOS:
    Las acciones hechas en Django Admin:
        - se reflejan automáticamente en la BD
        - pueden verse en SQLite Explorer

Resumen:
    - Django Admin permite crear sistemas CRUD completos sin frontend
    - Los modelos definen la estructura
    - Admin genera formularios automáticamente
    - Usuarios y grupos controlan el acceso
    - Ideal para sistemas internos como reservas
PERMISOS EN DJANGO (AUTHORIZATION)

Concepto:
    Los permisos controlan qué acciones puede realizar cada usuario.
    Funcionan de forma similar a roles en la vida real (ej: cliente vs personal).
    Django incluye un sistema de permisos integrado en django.contrib.auth.

TIPOS DE USUARIOS (a nivel permisos):
    Superuser:
        - Tiene TODOS los permisos
        - Puede gestionar usuarios, grupos y datos
        - Incluye permisos custom y automáticos

    Staff:
        - Puede acceder al admin
        - NO tiene permisos sobre modelos por defecto
        - Los permisos deben asignarse explícitamente

    Usuario normal:
        - No puede acceder al admin
        - Solo puede hacer lo que la app permita

    is_active:
        - Usuario activo por defecto
        - Si está en False, no puede autenticarse

CREACIÓN DE USUARIOS (conceptual):
    - Los usuarios son objetos Python
    - Se pueden crear desde:
        - Admin
        - Django shell
    - Para dar acceso al admin:
        user.is_staff = True

    Superuser:
        Se crea con:
            python manage.py createsuperuser

PERMISOS AUTOMÁTICOS DE MODELOS:
    Django crea permisos automáticamente por cada modelo.

    Tipos:
        - add
        - change
        - delete
        - view

    Formato del permiso:
        app.action_model

Ej:
    App: myapp
    Model: MyModel

    Permisos creados:
        myapp.add_mymodel
        myapp.change_mymodel
        myapp.delete_mymodel
        myapp.view_mymodel

CHECKEAR PERMISOS EN CÓDIGO:
    Se puede verificar permisos desde Python.

    request.user.has_perm('myapp.add_mymodel')

    Retorna:
        True / False

    Si no tiene permiso:
        - se puede lanzar PermissionDenied
        - o bloquear la lógica de la vista

GRUPOS:
    Un grupo es un conjunto de permisos.
    Un usuario puede pertenecer a múltiples grupos.

Ventajas:
    - Evita asignar permisos uno por uno
    - Facilita manejo de muchos usuarios
    - Permisos centralizados por rol

Ej conceptual:
    Grupo: staff
        - add_reservation
        - change_reservation
        - view_reservation

    Grupo: managers
        - add
        - change
        - delete
        - view

    Al asignar un usuario a un grupo:
        - hereda todos los permisos del grupo

IMPORTANTE:
    - Los permisos de grupo NO impiden permisos individuales
    - Un usuario puede tener permisos directos + permisos por grupo

USAR PERMISOS EN VISTAS:
    Django provee decoradores para proteger vistas.

    @permission_required('myapp.add_mymodel')
    def my_view(request):
        ...

    Si el usuario no tiene permiso:
        - acceso denegado automáticamente

Resumen:
    - Django maneja permisos de forma integrada
    - Los modelos generan permisos automáticamente
    - Superuser tiene todos los permisos
    - Staff necesita permisos explícitos
    - Grupos simplifican la gestión de permisos
    - has_perm permite validar permisos en código


ENFORCING PERMISSIONS (APLICAR PERMISOS EN DJANGO)

Idea clave:
    Tener permisos definidos NO es suficiente.
    Hay que ENFORZARLOS en el código para que realmente se respeten.
    Django permite aplicar permisos en:
        - vistas
        - templates
        - URLs
        - vistas basadas en clases

CUSTOM PERMISSIONS EN MODELOS:
    Además de los permisos automáticos (add, change, delete, view),
    se pueden definir permisos custom en el modelo.

Ej:
    class Product(models.Model):
        name = models.TextField()
        category = models.TextField()

        class Meta:
            permissions = [
                ('can_change_category', 'Can change category')
            ]

    Este permiso aparece luego en el Admin y puede asignarse a usuarios o grupos.

IMPORTANTE:
    Los modelos NO validan permisos por sí solos.
    El usuario llega al sistema a través del request.
    Por eso, los permisos se aplican principalmente en las vistas.

ENFORZAR PERMISOS EN VISTAS (FUNCTION-BASED)

1) Bloquear usuarios anónimos manualmente:
    from django.core.exceptions import PermissionDenied

    def myview(request):
        if request.user.is_anonymous:
            raise PermissionDenied()

2) login_required:
    Permite acceso solo a usuarios autenticados.

    from django.contrib.auth.decorators import login_required

    @login_required
    def myview(request):
        ...

3) user_passes_test:
    Permite definir una función custom que retorna True / False.

    def testpermission(user):
        return (
            user.is_authenticated and
            user.has_perm('myapp.can_change_category')
        )

    from django.contrib.auth.decorators import user_passes_test

    @user_passes_test(testpermission)
    def change_category(request):
        ...

    Se puede definir:
        login_url='login'

4) permission_required:
    Enforce directo de un permiso específico.

    from django.contrib.auth.decorators import permission_required

    @permission_required('myapp.can_change_category')
    def change_category(request):
        ...

ENFORZAR PERMISOS EN CLASS-BASED VIEWS:

    Se usa PermissionRequiredMixin.

    from django.contrib.auth.mixins import PermissionRequiredMixin
    from django.views.generic import ListView

    class ProductListView(PermissionRequiredMixin, ListView):
        permission_required = 'myapp.view_product'
        model = Product
        template_name = 'product.html'

ENFORZAR PERMISOS EN TEMPLATES:

    Django expone automáticamente:
        user
        perms

Ej:
    {% if user.is_authenticated %}
        Contenido para usuarios logueados
    {% endif %}

    {% if perms.myapp.can_change_category %}
        Contenido solo para usuarios con permiso
    {% endif %}

    Esto NO bloquea la vista, solo el contenido visual.

ENFORZAR PERMISOS EN URLS:

    Útil cuando la URL apunta directamente a una vista o página.

    from django.contrib.auth.decorators import login_required, permission_required

    urlpatterns = [
        path('users/', login_required(myview)),
        path(
            'category/',
            permission_required(
                'myapp.can_change_category',
                login_url='login'
            )(myview)
        ),
    ]

Resumen:
    - Los permisos se definen, pero se deben aplicar explícitamente
    - Se pueden aplicar en vistas, templates y URLs
    - permission_required es la forma más directa
    - user_passes_test permite lógica custom
    - PermissionRequiredMixin se usa en CBV
    - En templates solo controla visibilidad, no seguridad real

PERMISOS – GESTIÓN DESDE DJANGO SHELL
    Además del Admin, los permisos pueden gestionarse programáticamente desde el Django shell.
    El User tiene dos relaciones importantes:
        - groups
        - user_permissions

    Los permisos son objetos y pueden agregarse o quitarse dinámicamente.

    Crear usuario desde shell:
        from django.contrib.auth.models import User
        user = User.objects.create_user(
            username="mario",
            email="mario@littlelemon.com",
            password="password123"
        )

    Obtener usuario existente:
        user = User.objects.get(username="mario")

    Los permisos por defecto (add, change, delete, view) se crean automáticamente
    para cada modelo cuando se ejecuta:
        python manage.py migrate

    Gestión de permisos sobre el usuario:
        user.user_permissions.add(perm)      # agrega permiso
        user.user_permissions.remove(perm)   # quita permiso
        user.user_permissions.set([perm1])   # reemplaza permisos
        user.user_permissions.clear()        # elimina todos

    Los permisos pueden asignarse:
        - directamente al usuario
        - o indirectamente a través de grupos

    Si un usuario pertenece a un grupo, hereda automáticamente
    todos los permisos del grupo, pero puede tener permisos adicionales propios.

    El uso de grupos es la forma recomendada para manejar permisos
    cuando hay muchos usuarios con roles similares.

    
"""