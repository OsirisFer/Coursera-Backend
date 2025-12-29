# Functions pieza de codigo modular que realiza una tarea especifica
def funcion_ejemplo(param1, param2):
    """Esta es una función de ejemplo que suma dos números y devuelve el resultado."""
    resultado = param1 + param2
    return resultado

print("La suma da ",funcion_ejemplo(5, 3))  # Llama a la función y muestra el resultado
# Una variable es global si se define fuera de una función, enclosed si se define dentro de una función dentro de otra función
# y local si se define dentro de una función 
# Estructuras de datos en Python, estan las built-in y las definidas por el usuario
# Built-in son las que vienen con Python como lists, tuples, diccionaries, sets
# Definidas por el usuario son las que se crean usando clases, stack, queue, linked list, tree, graph, hashmap

# Contenedores son Arrays, Listas, Tuplas, Diccionarios, Conjuntos. 
# ARRAY la sintaxis del array en python es nombre = [elem1, elem2, elem3]

# LISTS  es igual que un array pero puede contener elementos de diferentes mutables, es indexado
list = [1, 2, 3, 4, 5]; 
list.insert(len(list), 6) # insert(posicion_a_insertar, valor_a_insertar)
list.extend([7, 8, 9]) # agrega multiples elementos al final de la lista
list.remove(1) # elimina el primer elemento con valor 1
list.pop(0) # elimina el elemento en la posicion 0 y  lo 
list[1] = 10 # modifica el valor del elemento en la posicion 0
del list[0] # elimina el elemento en la posicion 0 sin devolverlo


print(*list, sep=" , ") # imprime todos los elementos del array y sep es el separador 

# TUPLE es como una lista pero es INMUTABLE, la diferencia es el parentesis ()
# Usando type puedo ver que tipo de contenedor es
tuple = (1, "dos", 3.0, True)
tuple.index(3.0) # devuelve la posicion del elemento 3.0
print(list[0]) # imprime el primer elemento del array


# Dictionary es una colección de pares clave-valor y puede tener diferentes tipos de datos
dictionary = {"clave1": "valor1", "clave2": "valor2"} #usa llaves {}
print(dictionary["clave1"]) # imprime el valor asociado a la clave1
for key, value in dictionary.items(): # uso items si quiero recorrer clave y valor
    print(f"Clave: {key}, Valor: {value}")


# SET elementos únicos sin orden específico, no indexado, usa llaves {}
set = {1, 2, 2, 3, 4} # los elementos duplicados se eliminan automáticamente
set.add(5) # agrega un elemento al set
set.remove(2) # elimina el elemento 2 del set
set2 = {4, 5, 6, 7}
union_set = set.union(set2) # une dos sets
union_intersection = set.intersection(set2) # interseccion de dos sets
union_difference = set.difference(set2) # diferencia entre dos sets
print("Set unido: ", union_set, "Intersección: ", union_intersection, "Diferencia: ", union_difference)

# KWARGS es una forma de pasar un número variable de argumentos nombrados a una función
# Es decir que puedes pasar cualquier cantidad de pares clave-valor
def funcion_con_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(str(key) + ": " + str(value))
 
funcion_con_kwargs(nombre="Juan", edad=30, ciudad="Madrid")

# ARGS es una forma de pasar un número variable de argumentos posicionales a una función
# La diferencia con kwargs es que no se pasan pares clave-valor sino solo valores
def funcion_con_args(*args):
    for arg in args:
        print(arg)

funcion_con_args(1, 2, 3, 4, 5)

# Syntax errors son errores en la sintaxis del código como identación incorrecta o mal escrito
# Exceptions son errores que ocurren durante la ejecución del programa como dividir por cero o acceder a un índice fuera de rango
# try y except se usan para manejar excepciones y evitar que el programa se detenga abruptamente
try:
    resultado = 10 / 0
except ZeroDivisionError as error:
    print("Error: División por cero no permitida.", error)
except Exception as e:
    print("Error: División por cero no permitida.", e)
    print(e.__class__)  # Muestra el tipo de excepción
except IndexError as ie:
    print("Error: Índice fuera de rango.", ie)
except FileNotFoundError as fnfe:
    print("Error: Archivo no encontrado.", fnfe)
