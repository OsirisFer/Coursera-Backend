# Paradigmas en python: Programación Orientada a Objetos (POO), Funcional y Procedural
# Procedural funciona con funciones o subrutinas, la idea es DRY (Don't Repeat Yourself), es decir no repetir código
# Hacer muchas funciones pequeñas faciles de entender y reutilizar
# Map y Filter son funciones de orden superior que permiten aplicar una función a una lista o iterable
# Map aplica una función a cada elemento de un iterable y devuelve un nuevo iterable con los resultados
menu = [ "espresso", "latte", "cappuccino", "americano" ]

def find_coffee(coffee):
    if coffee[0] == "c":
        return coffee
map_coffees = map(find_coffee, menu)
print(map_coffees)  # <map object at 0x7f8c8c8c8c10>
for coffee in map_coffees:
    print(coffee)  # cappuccino

# Filter aplica una función a cada elemento de un iterable y devuelve un nuevo iterable con los elementos devueltos como True
filter_coffees = filter(find_coffee, menu)
print(filter_coffees)  # <filter object at 0x7f8c
for coffee in filter_coffees:
    print(coffee)  # cappuccino

# List Comprehensions son una forma concisa de crear una secuencia (lista, conjunto, diccionario) a partir de otra secuencia
data = [1, 2, 3, 4, 5] 
# la sintaxis es: [<expresión> for <elemento> in <secuencia> if <condición>]
squared = [x+3 for x in data if x % 2 == 0]
print(squared)  # [5, 7]

# Dictonary Comprehensions tienen la siguiente sintaxis: {<clave>: <valor> for <elemento> in <secuencia> if <condición>}
squared_dict = {x: x**2 for x in data if x % 2 == 0} 
print(squared_dict)  # {2: 4, 4: 16}
# otro ejemplo

# Set Comprehensions tienen la siguiente sintaxis: {<expresión> for <elemento> in <secuencia> if <condición>}
squared_set = {x**2 for x in data if x % 2 == 0}
print(squared_set)  # {16, 4}

# PARA ACCEDER A OBJETO USAMOS . Y PARA DICCIONARIOS USAMOS []
ejemploDiccionario = {"nombre": "Ana", "edad": 25, "ciudad": "Barcelona"}
print(ejemploDiccionario["nombre"])  # Ana

# Ejemplo objeto ahora para acceder a sus atributos usamos .
class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
persona1 = Persona("Luis", 30, "Madrid")
print(persona1.nombre)  # Luis

# POO 