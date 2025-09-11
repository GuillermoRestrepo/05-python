"""  TIPOS DE DATOS  """

"""  TYPE
Sirve para ver el tipo de dato de una variable o constante:
    type(Variable/Constante)
""" 
#    BASICOS
# ENTERO (int)
entero= 12
print(type(entero))

# DECIMAL (float)
decimal= 1.2
print(type(decimal))

# CADENA (str)
texto= "Hola"
print(type(texto))

# Booleano (bool)
booleano= True
print(type(booleano))

#    ESTRUCTURA DE DATOS
# TUPLA - (tuple)
tupla= ('a', 'b', 1, 2)
print(type(tupla))

# LISTA - (list)
lista= ['C', 'D', 3, 4]
print(type(lista))

# DICCIONARIO - (dict)
diccionario= {
    "nombre": "Alejandro",
    "edad": 25
}
print(type(diccionario))

# CONJUNTO - (set)
conjunto= {1, 2, 3, 3, 4, 5}
print(type(conjunto))

#    ESPECIALES
# VACIO - (NONE)
vacio= None
print(type(vacio))

# NUMEROS COMPLEJOS - (complex)
complejo= 12-3j
print(type(complejo))