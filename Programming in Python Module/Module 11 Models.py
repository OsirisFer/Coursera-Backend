"""
MODELS
    Son el equivalente a las tablas en las bases de datos. Cada modelo es una clase de python con atributos que representan fields en la bd.
    Django simplifica el CRUD con metodos ya existentes, eliminando la necesidad de las queries.
    Para crear una table en la bd se define una model class y django automaticamente maneja la clave primaeria. Las migraciones
    son necesarias para aplicar el model a la base de datos.

Estructura: todas las clases de modelos deben heredar de models.Model, cada atributo representa una columna, y cada instancia del modelo una fila
    Ej:
    from django.db import models
    class Persona(models.Model):
        nombre = models.CharField(max_length=50)
        edad = models.IntegerField()
Atributos de texto:
    models.CharField(max_length=100)   # texto corto (obligatorio max_length)
    models.TextField()                # texto largo
    models.EmailField()               # emails
    models.URLField()                 # URLs

Atributos numericos:
    models.IntegerField()
    models.FloatField()
    models.DecimalField(max_digits=10, decimal_places=2)

Atributos fecha y hora:
    models.DateField()
    models.DateTimeField()
    models.TimeField()

Utilidades:
    models.DateTimeField(auto_now=True)      # se actualiza al guardar
    models.DateTimeField(auto_now_add=True)  # se setea al crear
    models.BooleanField(default=False)
    models.CharField(
        max_length=50,
        null=True,      # permite NULL en la BD
        blank=True      # permite vacío en formularios
    )
    models.CASCADE    # borra los dependientes que contienen la foreign key
    models.PROTECT    # impide el borrado
    models.RESTRICT   # error si hay referencias, previene el borrado 
    models.SET_NULL   # setea NULL (requiere null=True)
    models.SET_DEFAULT
    EJ: 
    models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT
    )
    models.CharField(max_length=50, unique=True) # Campo unico
    models.CharField(max_length=50, db_index=True) #Indice
    class Meta:
        unique_together = ("campo1", "campo2")



Primary Key: Si no se define, Django automaticamente crea una id autoincremental, de lo contrario se define:
    id = models.AutoField(primary_key=True)  

ONE TO ONE
    models.OneToOneField(
        OtroModelo,
        on_delete=models.CASCADE #obligatorio en relaciones
    )
        class Persona(models.Model):
        nombre = models.CharField(max_length=50)

        class DNI(models.Model):
            persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
            numero = models.CharField(max_length=20)


ONE TO MANY
    models.ForeignKey(
        OtroModelo,
        on_delete=models.CASCADE
    )   
        class Categoria(models.Model):
            nombre = models.CharField(max_length=50)

        class Producto(models.Model):
            nombre = models.CharField(max_length=50)
            categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


MANY TO MANY 
    models.ManyToManyField(OtroModelo)
        class Alumno(models.Model):
            nombre = models.CharField(max_length=50)

        class Materia(models.Model):
            nombre = models.CharField(max_length=50)
            alumnos = models.ManyToManyField(Alumno) #django automaticamente crea una tabla intermedia


MIGRACIONES 
    Cada vez que cambio un modelo y tengo que actualizar la base de datos uso usando los siguientes comandos en el shell:
    python manage.py makemigrations     # detecta cambios en los modelos, y crea el archivo de migracion
    python manage.py migrate            # ejectuta las migraciones pendiente y modifica la base de datos de verdad
    python manage.py showmigrations     # muestra todas las migraciones
    python manage.py sqlmigrate myapp 0001_initial  #muestra el SQL real que django va a ejecutar, pero es infromativo no modifica nada

Las migraciones tienen version de control es decir se puede volver para atras con el siguiente comando a una migracion x, deshaciendo las previas:
    python manage.py migrate myapp 0002_nombre

ORM: Es una forma de usar querys basicamente en vez de SQL
    Los modelos son tablas, los objetos filas y el objects es el manager. ej: tabla.objects

Queryset es el resultado de la consulta select. ej: 
    Cliente.objects.all()
    Cliente.objects.filter(nombre="Juan")

    Traer todos     
        Cliente.objects.all()

    Traer 1
        Cliente.objects.get(pk=1)

    Filtrar
        Cliente.objects.filter(nombre__startswith="J")

    Create
        Cliente.objects.create(nombre="Ana")
    o sino:
        c = Cliente(nombre="Ana")
        c.save()

    Update
        c = Cliente.objects.get(pk=1)
        c.nombre = "Pedro"
        c.save()
 
    Delete 
        c = Cliente.objects.get(pk=1)
        c.delete()

DJANGO FORMS

Los formularios en Django se usan para recolectar datos del usuario desde HTML y enviarlos al servidor para su procesamiento.
Django maneja formularios usando la clase Form, que define la estructura, validación y procesamiento del formulario.
Los Form Fields definen:     - el tipo de dato esperado, cómo se muestra el campo en HTML,  validaciones básicas automáticas
Los fields en forms son distintos a los fields de models, pero cumplen un rol similar.

Estructura básica:
    from django import forms

    class CustomerForm(forms.Form):
        name = forms.CharField()
        age = forms.IntegerField()

Form Fields comunes:
    forms.CharField()           # texto (equivalente a <input type="text">)
    forms.EmailField()          # email (<input type="email">, valida formato)
    forms.IntegerField()        # números enteros (<input type="number">)
    forms.MultipleChoiceField() # selección múltiple (<select>)
    forms.ChoiceField()         # selección simple
    forms.FileField()           # subida de archivos (<input type="file">)
    forms.DateField()           # fechas

Argumentos comunes a todos los fields:
    required   # por defecto True
    label      # texto del label
    initial    # valor inicial
    help_text  # texto descriptivo de ayuda

Ej:
    class ApplicationForm(forms.Form):
        name = forms.CharField(label='Name of Applicant', max_length=50)
        address = forms.CharField(label='Address', max_length=100)

        posts = (
            ('Manager', 'Manager'),
            ('Cashier', 'Cashier'),
            ('Operator', 'Operator'),
        )
        field = forms.ChoiceField(choices=posts)

Validación:
    Los form fields tienen validación básica automática.
    Ej:
        EmailField valida que el formato sea correcto.
        Si el valor no es válido, Django muestra errores automáticamente.

Widgets:
    Los widgets controlan cómo se renderiza el campo en HTML.

Ej:
    forms.CharField(
        widget=forms.Textarea
    )

Modificar atributos del widget:
    forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5})
    )

Esto cambia el tamaño visual del campo.

Ejemplo DateField con calendario:
    forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

ChoiceField:
    Se define usando una constante con opciones.

    CHOICES = [
        ('pizza', 'Pizza'),
        ('pasta', 'Pasta'),
        ('salad', 'Salad'),
    ]

    forms.ChoiceField(choices=CHOICES)

Mostrar opciones como radio buttons:
    forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect
    )

RENDERIZADO DEL FORM:
    Una instancia del Form se convierte en HTML automáticamente.

    f = ApplicationForm()
    print(f)   # devuelve HTML de los campos (sin <form>)

Template básico:
    <form action="/form" method="POST">
        {% csrf_token %}
        {{ form }}
    </form>

Formas de renderizar:
    {{ form }}          # por defecto como tabla
    {{ form.as_table }} # envuelto en <tr>
    {{ form.as_p }}     # envuelto en <p>
    {{ form.as_ul }}    # envuelto en <li>
    {{ form.as_div }}   # envuelto en <div>

VIEW – PROCESAR FORMULARIO:
    En la vista se recibe el POST y se valida el formulario.

    from .forms import ApplicationForm

    def index(request):
        if request.method == 'POST':
            form = ApplicationForm(request.POST)
            if form.is_valid():
                # procesar datos
                pass
        else:
            form = ApplicationForm()

        return render(request, 'form.html', {'form': form})

VALIDACIÓN Y DATOS LIMPIOS:
    form.is_valid():
        Ejecuta validaciones de todos los fields.

    form.cleaned_data:
        Devuelve los datos ya validados y convertidos a tipos Python.

Ej:
    name = form.cleaned_data['name']
    address = form.cleaned_data['address']
    post = form.cleaned_data['posts']
    
Resumen:
    - Form = estructura y lógica del formulario
    - Form Fields = tipo de dato + validación + visual
    - Widgets controlan cómo se ve el campo en HTML
    - Django valida automáticamente los datos
    - Elegir bien el field es clave para formularios correctos
    - forms.Form permite crear formularios desde Python
    - Los fields definen tipo, validación y visual
    - Las vistas envían el form al template
    - El template renderiza el form con {{ form }}
    - Django incluye validación y seguridad (CSRF)
    - as_p, as_table y as_ul controlan el layout

FORM DJANGO – 

forms.py
    Acá se define el formulario.
    Es una clase Python que hereda de forms.Form.
    Define:
        - qué campos tiene el form
        - qué tipo de datos acepta
        - validaciones básicas
    Django usa esta clase para generar el HTML del formulario.

views.py
    Acá se maneja la lógica.
    La vista:
        - crea una instancia del formulario
        - la envía al template
        - más adelante procesa los datos (POST)
    Es el puente entre el form y la página HTML.

templates/home.html
    Es la parte visual.
    Renderiza el formulario que llega desde la vista.
    Usa:
        {{ form }} o {{ form.as_p }}
    Incluye:
        - <form method="POST">
        - csrf_token
        - botón submit

urls.py
    Conecta una URL con la vista.
    Define en qué ruta se muestra el formulario.
    Sin esto, el navegador no puede acceder al form.

settings.py
    Registra la app en INSTALLED_APPS.
    Le dice a Django que la app (y sus forms) existen.

Flujo completo (cómo interactúan):
    Usuario entra a la URL
        ↓
    urls.py llama a la vista
        ↓
    views.py crea el form (forms.py)
        ↓
    views.py envía el form al template
        ↓
    home.html muestra el formulario al usuario
        ↓
    Usuario completa y envía el form


        
"""

