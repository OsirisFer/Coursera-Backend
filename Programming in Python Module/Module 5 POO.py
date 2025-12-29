# En POO las clases tienen la siguiente estructura básica
# Encapslación: Agrupar datos y métodos que operan sobre esos datos dentro de una misma unidad (clase)
# En Python en realidad no hay atributos privados o protegidos, pero se usan convenciones en los nombres:

class NombreClase:
    def __init__(self, atributo1, atributo2):
        self._atributo1 = atributo1 # Este atributo es protegido porque empieza con _
        self.__atributo2 = atributo2  # Este atributo es privado porque empieza con __

    def metodo1(self):
        return f"Atributo1 es {self.atributo1}"

    def metodo2(self, valor):
        self.atributo2 = valor
        return f"Atributo2 actualizado a {self.atributo2}"
    
# Abstracción: Ocultar detalles complejos y mostrar solo la funcionalidad esencial
# Polimorfismo: distintos objetos usan el mismo método y python reconosce quien llama y ejecuta el comportamiento adecuado
# Es decir mismo método comportamiento diferente según el objeto que lo llama
class Perro:
    def hablar(self): #self lo que hace es referirse al objeto que llama al método
        return "Guau!"

class Gato:
    def hablar(self):
        return "Miau!"

def hacer_hablar(animal):
    print(animal.hablar())   # No importa qué animal es

p = Perro()
g = Gato()

hacer_hablar(p)   # Guau!
hacer_hablar(g)   # Miau!

# Herencia: Permite crear una nueva clase basada en una clase existente
class Animal:
    def __init__(self, nombre): #Init sirve para inicializar los atributos del objeto
        self.nombre = nombre

    def hablar(self):
        pass  # Método genérico

class Perro(Animal):
    def hablar(self):
        return "Guau!"
class Gato(Animal):
    def hablar(self):
        return "Miau!"
class Pato(Animal):
    def hablar(self):
        return "Cuac!"
dog = Perro("Firulais")
cat = Gato("Michi")
duck = Pato("Pato Lucas")

print(dog.hablar())  # Guau!
print(cat.hablar())  # Miau!
# Es decir gato y perro heredan el hablar de animal siendo cada uno de una clase diferente con su propio comportamiento
# issubclass() sirve para comprobar si una clase es subclase de otra
# isinstance() sirve para comprobar si un objeto es instancia de una clase

# super() lo que hace es llamar a un método de la clase padre desde la clase hija
class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)


class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print('Apple is sweet')

apple = FruitFlavour()

""" Una clase abstracta se usa para definir reglas que las clases hijas deben cumplir, especialmente qué 
métodos tienen que implementar, y sirve para evitar errores silenciosos. Sin clases abstractas, Python 
permite crear objetos aunque falten métodos importantes, lo que puede hacer que el programa “funcione” 
pero esté mal. Con una clase abstracta, Python lanza un error apenas intentás instanciar una clase que no 
implementó todo lo obligatorio, detectando el problema temprano. No se usa para inicializar variables, 
sino para garantizar comportamiento y diseño correcto, sobre todo cuando hay varias clases del mismo tipo 
y ciertas operaciones son indispensables.
"""

#MRO (Method Resolution Order) es el orden en que Python busca métodos y atributos en una jerarquía 
# de clases con herencia múltiple. De abajo hacia arriba y de izquierda a derecha.