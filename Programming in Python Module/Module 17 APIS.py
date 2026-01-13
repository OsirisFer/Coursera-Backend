"""API Endpoint Naming – Buenas Prácticas

URI / Endpoint
- El endpoint define qué recurso expone el servidor.
- Debe ser claro, predecible y consistente.

Convenciones de nombres
- Usar siempre minúsculas.
- Separar palabras con guiones (-).
- No usar underscores, camelCase, PascalCase ni abreviaturas.
  Ej: /menu-items

Variables en la URL
- Los identificadores van en camelCase y entre {}.
  Ej:
    /orders/{orderId}
    /customers/{customerId}/orders

Jerarquía de recursos
- Usar "/" para indicar relaciones entre recursos.
  Ej:
    /orders/{orderId}/menu-items
    /books/{bookId}/author
    /authors/{authorId}/books

Usar sustantivos, no verbos
- Los endpoints representan recursos (nombres).
- Usar plural para colecciones.

Correcto:
  /orders
  /orders/{orderId}
  /books/{bookId}/price

Incorrecto:
  /getOrders
  /deleteUser
  /saveOrder
  /order

Acciones → HTTP methods
- GET: obtener
- POST: crear
- PUT / PATCH: actualizar
- DELETE: eliminar
- Las acciones NO van en el nombre del endpoint.

Evitar caracteres especiales
- No usar | ^ @ ! etc.
- Para múltiples valores, usar coma (,).

Correcto:
  /users/12,23,45/address

Incorrecto:
  /users/12|23|45/address

Evitar extensiones de archivo
- No usar .json o .xml en la URL.
- Usar query parameters para el formato.

Correcto:
  /orders/{orderId}?format=json
  /orders/{orderId}?format=xml

Incorrecto:
  /orders/{orderId}.json
  /orders/{orderId}.xml

Filtrado y búsqueda
- Usar query string parameters.

Ejemplos:
  /menu-items?category=appetizers
  /articles?per-page=10&page=2
  /users/{userId}/locations?country=USA

Trailing slash
- No usar slash final.

Correcto:
  /orders/{orderId}

Incorrecto:
  /orders/{orderId}/

Resumen
- Minúsculas y guiones
- Recursos como sustantivos
- Relaciones con "/"
- Acciones con HTTP methods
- Filtros y formatos con query params
- Sin extensiones ni trailing slash


Herramientas para probar APIs

Objetivo
- Permiten enviar requests HTTP y probar APIs sin escribir código.
- Funcionan en Windows, macOS y Linux.

curl (Command Line)
- Herramienta para hacer requests HTTP desde la terminal.
- No tiene interfaz gráfica.

GET:
  curl https://postman-echo.com/get

POST:
  curl -X POST -d "key=value" https://postman-echo.com/post

- Útil para pruebas rápidas y scripting.

Postman
- Herramienta gráfica para probar y depurar APIs.
- Permite enviar GET, POST, PUT, DELETE, etc.
- Facilita trabajar con headers, body, auth y collections.

Insomnia
- Cliente REST con interfaz gráfica (desktop).
- Permite guardar y organizar requests en collections.
- Usado para ejecutar y repetir llamadas a APIs fácilmente.

Uso básico en Insomnia
1. Crear una Request Collection.
2. Crear un HTTP Request.
3. Elegir método HTTP (GET, POST, etc.).
4. Ingresar la URL del endpoint.
5. (POST) Agregar datos en Body:
   - Form URL Encoded o JSON
6. Enviar request y ver la respuesta.

Ejemplo GET:
  https://httpbin.org/get?project=LittleLemon

Ejemplo POST:
  URL: https://httpbin.org/post
  Body (JSON o Form):
    project = LittleLemon

Resumen
- curl: terminal, rápido, sin UI.
- Postman: UI completa, testing y debugging.
- Insomnia: simple, organizado, ideal para practicar APIs.

REST API – Best Practices esenciales

KISS (Keep It Simple)
- Cada endpoint debe hacer UNA sola cosa.
- Evitar lógica compleja o múltiple en un mismo endpoint.
- Ej:
  PATCH /menu-items/{itemId}
  body: { "status": "On" | "Off" }

Filtrado, orden y paginación
- Permitir filtrar resultados grandes con query params.
  Ej:
    /menu-items?category=desserts
    /menu-items?sort=price&order=asc
- Usar paginación para grandes volúmenes.
  Ej:
    /menu-items?page=10&per-page=4

Versionado de API
- Cambios grandes requieren nueva versión.
- Mantener pocas versiones (idealmente 2).
  Ej:
    /api/v1/menu-items
    /api/v2/menu-items

Caching
- Cachear respuestas cuando los datos no cambian seguido.
- Enviar headers HTTP adecuados.
- Actualizar cache solo cuando el recurso cambia.
  Ej:
    GET /menu-items → respuesta cacheada

Rate limiting
- Limitar cantidad de requests por usuario/cliente.
  Ej:
    requests por minuto / hora / día
- Previene abuso del API.

Monitoring
- Monitorear:
  - Latencia
  - Status codes:
    - 4xx → errores del cliente
    - 5xx → errores del servidor
  - Uso de ancho de banda
- Detecta errores y abusos temprano.

Resumen
- APIs simples y enfocadas
- Filtrado + paginación
- Versionado controlado
- Caching consistente
- Rate limiting + monitoreo

REST API – Seguridad básica

HTTPS / SSL
- Usar siempre HTTPS, no HTTP.
- SSL cifra los datos entre cliente y servidor.
- Protege credenciales y datos sensibles en tránsito.

Signed URLs
- Permiten acceso temporal y controlado a un recurso.
- La URL incluye una firma que el servidor valida.
- Evita llamadas desde clientes no autorizados.

HMAC (firma de mensajes)
- Mecanismo común para generar firmas.
- Usa un secret key + algoritmo hash.
- Garantiza autenticidad e integridad del request.

Autenticación
- Evitar enviar usuario y contraseña en cada request.
- Preferir autenticación basada en tokens.
- Flujo típico:
  1. Login → usuario + password
  2. Servidor devuelve token
  3. Requests posteriores incluyen el token en headers

JWT (JSON Web Token)
- Estándar común para tokens.
- Contiene información del usuario firmada.
- El servidor valida el token en cada request.

Códigos HTTP relacionados
- 401 Unauthorized:
  - Credenciales inválidas o inexistentes.
- 403 Forbidden:
  - Credenciales válidas pero sin permisos.

CORS (Cross-Origin Resource Sharing)
- Controla qué dominios pueden llamar al API.
- Se configura mediante headers HTTP.
- Evita accesos no deseados desde otros orígenes.

Firewalls
- Restringen acceso por IP.
- Permiten aceptar requests solo desde IPs autorizadas.

Resumen
- HTTPS obligatorio
- Firmas y tokens para autenticación
- 401 ≠ 403
- Control de orígenes (CORS)
- Restricción por IP con firewalls

Debugging en Django con Visual Studio Code

Objetivo del debugging
- Encontrar y corregir errores de forma eficiente.
- Analizar el flujo del programa y los valores de las variables.
- Reproducir errores en un entorno controlado.

Preparación en VS Code
- Activar el entorno virtual:
  pipenv shell
- Abrir el proyecto en VS Code.
- Seleccionar el intérprete de Python correcto.
- Crear app Django y abrir el proyecto.

Configurar el debugger
- Abrir el panel de Run and Debug en la columna izquierda de vs code (icono de bug).
- Crear launch.json.
- Elegir configuración: Django.
- Opciones:
  - Start Debugging: inicia servidor + entorno virtual.
  - Run Without Debugging: ejecuta sin debugger.

Conceptos clave
- Breakpoint:
  - Punto donde se pausa la ejecución.
  - Se agrega con el punto rojo al lado del número de línea.
  Ejemplo:
    for i in range(10):
        if i % 2 == 0:   ← breakpoint aquí
            print(i)

- Watch:
  - Permite observar variables y sus cambios en tiempo real.
  Ejemplo:
    Variable observada: i
    Permite ver cómo cambia su valor en cada iteración.

Barra de herramientas de debug (con ejemplos)

- Continue / Pause:
  - Continúa la ejecución hasta el próximo breakpoint.
  Ejemplo:
    Pausa en línea 5 → Continue → salta al siguiente breakpoint.

- Step Over:
  - Ejecuta la línea actual y pasa a la siguiente.
  Ejemplo:
    x = 10        ← Step Over
    y = x + 5    ← se ejecuta sin entrar en funciones

- Step Into:
  - Entra dentro de una función.
  Ejemplo:
    result = calculate(x)  ← Step Into
    def calculate(x):      ← entra aquí

- Step Out:
  - Sale de la función actual y vuelve al punto donde fue llamada.
  Ejemplo:
    return total           ← Step Out → vuelve al caller

- Restart:
  - Reinicia toda la sesión de debugging.
  Ejemplo:
    Vuelve a ejecutar el servidor desde el inicio.

- Stop:
  - Detiene el debugging y apaga el servidor.
  Ejemplo:
    Finaliza la sesión de debug completamente.

Debugging de APIs con el Developer Console del navegador

Acceso al Developer Console
- Chrome:
  - Windows / Linux: Ctrl + Shift + I
  - macOS: Cmd + Option + I

Uso principal
- Depurar llamadas HTTP hechas desde JavaScript.
- Inspeccionar requests y responses de APIs.

Pestaña Network
- Filtrar por:
  - Fetch / XHR → muestra solo llamadas a APIs.
- Cada request queda registrada automáticamente.

Probar una API desde la consola
- Usar fetch() en la pestaña Console.
  Ejemplo:
    fetch('https://api.example.com/items')

- La llamada aparece en Network → Fetch/XHR.

Inspeccionar una llamada
- Headers:
  - Request headers
  - Response headers
- Preview:
  - Respuesta renderizada.
- Response:
  - Respuesta cruda (raw).
- Initiator:
  - Línea de JavaScript que disparó la llamada.

Opciones útiles
- Disable cache:
  - Fuerza respuestas sin cache.
- Clear:
  - Limpia las llamadas registradas.

Probar APIs directamente en el navegador
- Ejemplo:
  https://restcountries.com/v3.1/all
- El JSON puede verse sin formato.

Formatear JSON
- Usar una extensión JSON Formatter.
- Permite leer y explorar el JSON fácilmente.

Idea clave
- Network + Console permiten ver:
  - Qué se envía
  - Qué responde el servidor
  - Desde dónde se llama la API

  

  Mock APIs – Concepto y uso

Qué es un Mock API
- Un mock API imita un endpoint real.
- Devuelve datos falsos pero con la estructura correcta.
- No ejecuta lógica de negocio.
- Responde con datos hardcodeados o generados previamente.
Para qué se usa
- Permite que el frontend o clientes empiecen a desarrollar antes de que el API real exista.

Pasos para crear Mock APIs
1. Crear datos mock (estructura correcta, valores falsos).
2. Crear endpoints mock que devuelvan esos datos.

Herramientas comunes
- Mockaroo:
  - Generador de datos falsos.
  - https://www.mockaroo.com
- MockAPI:
  - Servicio para crear endpoints mock.
  - https://mockapi.io

API View Decorator (@api_view) – lo esencial

Qué es
- Un decorador de DRF para convertir una función normal en un endpoint REST real.

Dónde se usa
- Archivo: BookListAPI/views.py

Qué te permite hacer (lo importante)
- Devolver JSON fácilmente (con Response).
- Ver y probar la API desde el navegador (Browsable API).
- Definir qué métodos HTTP acepta el endpoint (GET, POST, etc.).
- DRF maneja status codes y headers correctamente.

Ejemplo mínimo

Archivo: BookListAPI/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def books(request):
    return Response({"message": "Listado de libros"})

Endpoint:
http://127.0.0.1:8000/api/books/

Agregar más métodos

@api_view(['GET', 'POST'])
def books(request):
    if request.method == 'GET':
        return Response({"message": "Listado"})
    if request.method == 'POST':
        return Response({"message": "Creado"})

Qué pasa automáticamente
- Si usás POST → aparece un formulario para enviar JSON en el navegador.
- Si usás un método no permitido → 405 Method Not Allowed.

Resumen ultra corto
- @api_view = función → API REST
- Response = JSON + status correcto
- Define métodos HTTP
- Te da API navegable sin herramientas externas

| Caso                 | Qué usar      |
| -------------------- | ------------- |
| Endpoint simple      | FBV           |
| Lógica personalizada | APIView       |
| CRUD común           | Generic Views |
| CRUD grande          | ModelViewSet  |

"""