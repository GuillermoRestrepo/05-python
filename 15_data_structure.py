"""  ESTRUCTURA DE DATOS  """
# LISTAS
numeros = [10, 20, 30, 40]
numeros.append(50)       # agrega un elemento
numeros.insert(1, 15)    # inserta en posición 1
numeros.remove(20)       # elimina el valor 20
ultimo = numeros.pop()   # elimina el último y lo devuelve
print(numeros[0])        # acceder por índice (10)
print(numeros[-1])       # acceder al último (40)
print(len(numeros))      # longitud


# TUPLAS
coordenada = (10, 20)
print(coordenada[0])  # 10


# CONJUNTOS
colores = {"rojo", "verde", "azul", "rojo"}
print(colores)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)  # unión → {1, 2, 3, 4, 5, 6}
print(A & B)  # intersección → {3, 4}
print(A - B)  # diferencia → {1, 2}
print(A ^ B)  # diferencia simétrica → {1, 2, 5, 6}


# DICCIONARIOS
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Quito"
}

print(persona["nombre"])      # acceder por clave
persona["edad"] = 26          # modificar valor
persona["profesion"] = "Dev"  # agregar nueva clave
del persona["ciudad"]         # eliminar clave
print(persona.keys())         # obtener todas las claves
print(persona.values())       # obtener todos los valores
print(persona.items())        # pares clave-valor