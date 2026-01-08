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


    

        
"""

