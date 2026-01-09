from django import forms

SHIFTS = (
    ('morning', 'Morning'),
    ('afternoon', 'Afternoon'),
    ('evening', 'Evening'),
)

class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    shift = forms.ChoiceField(choices=SHIFTS)
    time_log = forms.TimeField()

"""
CREACIÓN DE FORMS CON DJANGO (Forms API)

Concepto:
    Django permite crear formularios usando clases Python que generan automáticamente el HTML,
    aplican validaciones y agregan seguridad (CSRF).
    El proceso es muy similar a crear modelos.

Paso 1: Crear forms.py
    Dentro del directorio de la app se crea el archivo:
        forms.py

    Se importa forms desde Django y se crea una clase que hereda de forms.Form.

Ej:
    from django import forms

    SHIFTS = (
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
    )

    class InputForm(forms.Form):
        first_name = forms.CharField(max_length=200)
        last_name = forms.CharField(max_length=200)
        shift = forms.ChoiceField(choices=SHIFTS)
        time_log = forms.TimeField()

Paso 2: Crear la vista (views.py)
    Se importa el formulario y se crea una vista que lo envía al template.

    from .forms import InputForm

    def form_view(request):
        form = InputForm()
        context = {'form': form}
        return render(request, 'home.html', context)

Paso 3: Crear el template
    Se crea una carpeta templates dentro de la app.
    Se crea el archivo home.html.

Template básico:
    <form method="POST">
        {% csrf_token %}
        {{ form }}
        <input type="submit" value="Submit">
    </form>

    CSRF token:
        Es obligatorio para formularios POST.
        Protege contra ataques CSRF.

Paso 4: Configuración necesaria
    - Agregar la app en INSTALLED_APPS
    - Configurar urls.py (app y proyecto)
    - Ejecutar el servidor:
        python manage.py runserver

Renderizado del formulario:
    Django renderiza automáticamente los campos definidos en el Form.
    Por defecto se muestran como tabla.

Cambiar formato visual:
    {{ form.as_p }}    # renderiza cada campo dentro de <p>
    {{ form.as_table }}
    {{ form.as_ul }}

Ej:
    {{ form.as_p }}

Validación automática:
    Por defecto, todos los campos son obligatorios.
    Django valida automáticamente tipos de datos (ej: TimeField, EmailField).

Cambiar validación:
    first_name = forms.CharField(max_length=200, required=False)

Agregar ayuda al campo:
    time_log = forms.TimeField(
        help_text="Enter the exact time"
    )

Esto muestra texto descriptivo junto al campo.

Estilos:
    Se pueden aplicar estilos desde HTML o CSS.
    Ejemplo inline:
        <form style="background-color: lightgray">

Resumen:
    - forms.Form permite crear formularios desde Python
    - Los fields definen tipo, validación y visual
    - Las vistas envían el form al template
    - El template renderiza el form con {{ form }}
    - Django incluye validación y seguridad (CSRF)
    - as_p, as_table y as_ul controlan el layout

"""