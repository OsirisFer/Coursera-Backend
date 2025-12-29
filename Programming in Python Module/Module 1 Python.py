#!/usr/bin/python
import sys; x = 'foo'; sys.stdout.write(x + '\n') #el ; permite poner varias instrucciones en una sola linea
print("helloworld") #asi se imprime en Python
#print("helloworld") Asi se hace un comentario en Python
'''
otro  comentario
pero multilinea
'''

if 5 > 2: #condicionales
    print("cinco es mayor que dos")
elif 5 == 2: #else if
    print("cinco es igual a dos")
else: #else
    print("cinco es menor que dos")

#Python no tiene switch/case
#Python no tiene variables, las variables son referencias a objetos
x = 5 # crea una variable entera
y = "Hello, World!" # crea una variable string
# Constante
PI = 3.14 # en python no hay constantes reales, pero por convención se usan mayúsculas

# BOOLEANOS
is_true = True
is_false = False
print(type(is_false)) # imprime el tipo de dato
#Strings, es una secuencia de caracteres con 0 index, para saber el largo uso len
string = "Hello, World!" \
"hey " # concatenación para cadenas largas
print(string, len(string)) # imprime el largo del string
# Implicit Type Conversion  es cuando conviertes un tipo de dato a otro usando ej  str(), int(), float()
# INPUTS 
name = input("Enter your name: ") # input devuelve una string por eso si buscas otro tipo de dato debes castear
# Implicit Type Conversion es cuando Python convierte automaticamente un tipo de dato a otro ej sumando int + float = float
# Python tiene type safety por lo que si quiero sumar un int + str dara error
# Operadores logicos son and, or, not

# Ejemplo de condicionales con operadores logicos
if is_true and not is_false:
    print("Both conditions are true")
elif is_true or is_false:
    print("At least one condition is true")
else:
    print("Something else")

# MATCH STATMENT 
value = 2
match value:
    case 1:
        print("Value is 1")
    case 2:
        print("Value is 2")
    case _:
        print("Value is something else")

#LOOPS existen break que sirve para salir del loop y continue que sirve para saltar a la siguiente iteracion y pass que sirve para no hacer nada y que no de error
for i in range(5): # for loop de 0 a 4
    print(i)

while value < 5: # while loop
    print(value)
    value += 1 # incrementa value en 1

