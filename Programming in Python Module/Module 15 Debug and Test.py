"""TESTING EN DJANGO (UNIT TESTS)

CONCEPTO
    Testing ≠ debugging
    Testing evalúa:
        - calidad
        - confiabilidad
        - comportamiento esperado
    Usa pruebas automáticas con resultado:
        pass / fail / error

TIPO MÁS COMÚN
    Unit Testing
    Prueba unidades pequeñas:
        - funciones
        - métodos
        - modelos
        - vistas

BASE EN DJANGO
    Django usa unittest de Python
    Enfoque basado en clases

    Clase base:
        django.test.TestCase

UBICACIÓN DE TESTS
    Dentro de cada app:
        tests.py   (proyectos chicos)
    O archivos separados:
        test_models.py
        test_views.py

EJECUTAR TESTS
    Todos los tests:
        python manage.py test

    Tests de una app:
        python manage.py test reservations

    TestCase específico:
        python manage.py test reservations.tests.ReservationTestCase

    Método específico:
        python manage.py test reservations.tests.ReservationTestCase.test_seat_count

EJEMPLO: TESTEAR UN MODELO

models.py
    class Reservation(models.Model):
        first_name = models.CharField(...)
        last_name = models.CharField(...)
        booking_time = models.DateTimeField(auto_now=True)

tests.py
    from django.test import TestCase
    from datetime import datetime
    from .models import Reservation

    class ReservationModelTest(TestCase):

        @classmethod
        def setUpTestData(cls):
            Reservation.objects.create(
                first_name="John",
                last_name="Doe"
            )

        def test_fields_are_strings(self):
            obj = Reservation.objects.get(id=1)
            self.assertIsInstance(obj.first_name, str)
            self.assertIsInstance(obj.last_name, str)

        def test_timestamp(self):
            obj = Reservation.objects.get(id=1)
            self.assertIsInstance(obj.booking_time, datetime)

PASOS IMPORTANTES
    - Crear modelo
    - Migrar:
        python manage.py makemigrations
        python manage.py migrate
    - Crear tests en TestCase
    - Usar assert* para validar resultados
    - Ejecutar tests con manage.py test

RESULTADOS
    .  → test pasa
    F  → test falla
    AssertionError indica qué condición falló

IDEA CLAVE
    Django testing funciona igual que unittest de Python,
    pero integrado con:
        - ORM
        - base de datos de test
        - apps Django
"""