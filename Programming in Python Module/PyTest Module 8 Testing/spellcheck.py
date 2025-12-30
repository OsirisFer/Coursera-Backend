#Testing 
"""
Categrias de testing:
    Black Box Testing, es el tipo de testing en el que no se conoce la estructura interna del codigo,
    White Box Testing, es el tipo de testing en el que se conoce la estructura interna del codigo.

    Functional Testing: Se enfoca en verificar que las funciones del software operen de acuerdo a los requisitos especificados.
    Non-Functional Testing: Se enfoca en aspectos no funcionales del software, como el rendimiento, la usabilidad y la seguridad.
    Maintenance Testing: Se realiza para asegurar que las modificaciones o actualizaciones en el software no introduzcan nuevos errores.

    Unit Testing: Pruebas que se realizan a nivel de unidades o componentes individuales del software.
    Integration Testing: Pruebas que se realizan para verificar la interacción entre diferentes unidades o componentes del software.
    System Testing: Pruebas que se realizan en el sistema completo para verificar que cumple con los requisitos especificados.
    Acceptance Testing: Pruebas que se realizan para verificar que el software cumple con los criterios de aceptación definidos por el cliente o usuario final.

    Regression Testing: Pruebas que se realizan para asegurar que los cambios recientes en el software no hayan afectado negativamente las funcionalidades existentes.
    Automated Testing: Pruebas que se realizan utilizando herramientas automatizadas para ejecutar casos de prueba y comparar los resultados esperados con los resultados reales.
    Agregation Testing: Pruebas que se realizan para verificar la correcta integración y funcionamiento de múltiples componentes o sistemas que trabajan juntos.

"""




# Given implementations of some string-related methods. 
# DO NOT CHANGE THIS FILE

def word_count(sentence):
    # Function to check the number of words. Returns the word count in string.
    words = len(sentence.split())
    print(words)
    return words

def char_count(sentence):
    # Function to check the number of characters. Returns the character count in string.
    chars = len(sentence)
    print(chars)
    return chars

def first_char(sentence):
    # Function to check the first character using the string index. Returns the first character in string.
    first = sentence[0]
    return first

def last_char(sentence):
    # Function to check the last character using the string index. Returns the last character in string.
    last = sentence[-1]
    return last