"""CLASS-BASED GENERIC VIEWS (CBV)

CONCEPTO
    Django permite implementar vistas:
        - Function-Based Views (FBV)
        - Class-Based Views (CBV)

    Las Generic Views son CBVs ya preparadas
    para resolver casos comunes (CRUD) con menos código.

CLASE BASE
    Todas las CBVs usan:
        django.views.View
    y se conectan en URLs con:
        as_view()

EJEMPLO BÁSICO DE CBV
    class NewView(View):
        def get(self, request):
            return HttpResponse("response")

    urls.py:
        path('about/', NewView.as_view())

GENERIC VIEWS MÁS USADAS
    TemplateView   → renderizar templates
    CreateView     → crear registros
    ListView       → listar registros
    DetailView     → ver un registro
    UpdateView     → actualizar registro
    DeleteView     → eliminar registro
    LoginView      → autenticación

COMPARACIÓN FBV vs CBV

FBV – Ventajas
    - Más simples
    - Código explícito
    - Fáciles de leer
    - Decoradores directos
    - Útiles para lógica puntual

FBV – Desventajas
    - Difíciles de reutilizar
    - Mucho if/elif para métodos HTTP

CBV – Ventajas
    - Reutilizables
    - DRY
    - Separación clara por método HTTP
    - Muchas vistas genéricas ya implementadas

CBV – Desventajas
    - Flujo implícito
    - Más difíciles de leer al inicio
    - Decoradores requieren overrides

REGLAS DE GENERIC VIEWS
    - Se debe definir el modelo:
        model = Employee
    - Django busca templates con nombres estándar:
        employee_list.html
        employee_detail.html
        employee_form.html
        employee_confirm_delete.html

MODELO DE EJEMPLO
    class Employee(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField()
        contact = models.CharField(max_length=15)

CREATEVIEW
    Crea un nuevo registro automáticamente.

    class EmployeeCreate(CreateView):
        model = Employee
        fields = '__all__'
        success_url = "/employees/success/"

    Template:
        employee_form.html

LISTVIEW
    Lista todos los objetos del modelo.

    class EmployeeList(ListView):
        model = Employee

    Template:
        employee_list.html

    Contexto disponible:
        object_list

DETAILVIEW
    Muestra un solo objeto por PK.

    class EmployeeDetail(DetailView):
        model = Employee

    URL:
        path('show/<int:pk>', EmployeeDetail.as_view())

    Template:
        employee_detail.html

UPDATEVIEW
    Actualiza un objeto existente.

    class EmployeeUpdate(UpdateView):
        model = Employee
        fields = '__all__'
        success_url = "/employees/success/"

    URL:
        path('update/<int:pk>', EmployeeUpdate.as_view())

    Template:
        employee_update_form.html

DELETEVIEW
    Elimina un objeto con confirmación.

    class EmployeeDelete(DeleteView):
        model = Employee
        success_url = "/employees/success/"

    URL:
        path('delete/<int:pk>', EmployeeDelete.as_view())

    Template:
        employee_confirm_delete.html

IDEA CLAVE
    Generic Views permiten hacer CRUD completo
    con muy poco código, siguiendo convenciones.
"""