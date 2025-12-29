# Importamos ABC y abstractmethod desde el módulo abc
# ABC permite crear clases abstractas
# abstractmethod obliga a las clases hijas a implementar ciertos métodos
from abc import ABC, abstractmethod


# Clase Bank
# Es una clase abstracta (hereda de ABC)
# No se puede instanciar directamente
class Bank(ABC):

    # Método abstracto basicinfo
    # Las clases hijas DEBEN implementarlo
    # Aunque tenga código, igual no se puede usar si no se redefine
    @abstractmethod
    def basicinfo(self):
        print("This is a generic bank")
        return "Generic bank: 0"

    # Método abstracto withdraw
    # Define una "promesa": toda clase banco debe poder retirar dinero
    @abstractmethod
    def withdraw(self):
        pass


# Clase Swiss
# Es una clase concreta que hereda de Bank
# Como implementa TODOS los métodos abstractos, sí se puede instanciar
class Swiss(Bank):

    # Constructor (__init__)
    # Se ejecuta automáticamente cuando se crea un objeto Swiss
    # Inicializa el estado del objeto
    def __init__(self):
        self.bal = 1000  # balance inicial del banco

    # Implementación del método abstracto basicinfo
    # Reemplaza la versión definida en Bank
    def basicinfo(self):
        print("This is the Swiss Bank")
        return "Swiss Bank: " + str(self.bal)

    # Implementación del método abstracto withdraw
    # Permite retirar dinero del balance
    def withdraw(self, amount):

        # Si hay suficiente dinero
        if amount <= self.bal:
            self.bal = self.bal - amount   # se descuenta el monto
            print(self.bal, amount)
            return self.bal

        # Si no hay suficiente dinero
        else:
            print("Insufficient funds")
            return self.bal


# Código principal (driver code)
def main():

    # Verificación: Bank debe ser una subclase de ABC
    # Esto confirma que es una clase abstracta
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"

    # Creamos una instancia de Swiss
    # Bank NO se puede instanciar, Swiss sí
    s = Swiss()

    # Llamamos a basicinfo (polimorfismo)
    print(s.basicinfo())

    # Retiramos 30 (válido)
    s.withdraw(30)

    # Intentamos retirar más de lo disponible
    s.withdraw(1000)


# Punto de entrada del programa
# Garantiza que main() se ejecute solo si este archivo es el principal
if __name__ == "__main__":
    main()
"""
===========================================================
EXPLICACIÓN GENERAL DEL PROGRAMA Y CONCEPTOS UTILIZADOS
===========================================================

¿QUÉ HACE ESTE PROGRAMA?
-----------------------
Este programa implementa un ejemplo simple de un sistema bancario
utilizando Programación Orientada a Objetos (POO).

Existe una clase abstracta llamada Bank que define qué comportamientos
mínimos debe tener cualquier banco (mostrar información y retirar dinero),
pero no define cómo se hacen exactamente esas operaciones.

La clase Swiss hereda de Bank y proporciona una implementación concreta
de esos comportamientos, manejando un balance y permitiendo retiros
con validación de fondos.

El programa principal crea una instancia de Swiss, muestra información
del banco y realiza operaciones de retiro, incluyendo el caso donde
no hay fondos suficientes.


CONCEPTOS CLAVE UTILIZADOS
-------------------------

1) CLASES ABSTRACTAS (ABC)
   - Se usan para definir una estructura común o contrato.
   - Evitan que se creen objetos incompletos.
   - Garantizan que todas las clases hijas tengan ciertos métodos.

   En este caso:
   Bank define qué debe hacer un banco, pero no cómo.

2) @abstractmethod
   - Obliga a que las clases hijas implementen ciertos métodos.
   - Si una clase no los implementa, Python no permite instanciarla.

   Esto asegura que todos los bancos tengan basicinfo() y withdraw().

3) HERENCIA
   - Permite que una clase reutilice la estructura de otra.
   - Representa una relación "es un".

   Swiss es un Bank.

4) POLIMORFISMO
   - Permite que distintos objetos respondan al mismo método
     de formas distintas.
   - Se llama al método sin preocuparse por la clase concreta.

   basicinfo() y withdraw() existen en Bank, pero se ejecutan
   con la lógica de Swiss.

5) CONSTRUCTOR (__init__)
   - Se ejecuta cuando se crea el objeto.
   - Inicializa el estado del objeto.

   En este programa define el balance inicial del banco.

6) ENCAPSULAMIENTO
   - Los datos pertenecen al objeto.
   - El balance solo se modifica mediante métodos.

7) VALIDACIONES Y CONTROL DE FLUJO
   - Se verifica si hay fondos suficientes antes de retirar.
   - Se evita modificar el estado del objeto en situaciones inválidas.


¿POR QUÉ SE USAN ESTAS COSAS EN PROGRAMAS REALES?
-------------------------------------------------

- Para evitar errores:
  Las clases abstractas garantizan que las implementaciones sean completas.

- Para mantener el código ordenado:
  Separan la definición del comportamiento de su implementación.

- Para facilitar mantenimiento y escalabilidad:
  Se pueden agregar nuevos tipos de bancos sin modificar el código existente.

- Para trabajar en equipo:
  Un desarrollador define el contrato (Bank) y otros implementan
  distintas variantes (Swiss, InternationalBank, DigitalBank, etc.).

- Para escribir código más claro y profesional:
  El diseño refleja mejor conceptos del mundo real.

- Para permitir extensiones futuras:
  Nuevas clases pueden reutilizar la misma interfaz sin romper el sistema.


RESUMEN FINAL
-------------
Bank define las reglas.
Swiss implementa las reglas.
El programa usa esas reglas sin depender de una implementación específica.

Esto es uno de los pilares de la Programación Orientada a Objetos.
===========================================================
"""
