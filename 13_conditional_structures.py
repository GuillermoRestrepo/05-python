"""  ESTRUCTURA CONDICIONALES  """
edad= 18

# IF
if edad >= 18:
    print("Mayor de edad")

# IF - ELSE
edad_2= 15
if edad_2 >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

# ELIF
nota= 63
if nota < 40:
    print("Reprobado")
elif nota >= 40 and nota < 70:
    print("Recuperacion")
else:
    print("Aprobado")

# IF (ternario): condicio de una sola linea
estado= 0
mensaje= "Encendido" if estado == 1 else "Apagado"
print(mensaje)

# MATCH - CASE
opcion= 7
match opcion:
    case 1:
        print("Opcion 1")
    case 2:
        print("Opcion 2")
    case 3:
        print("Opcion 3")
    case _:
        print("Opcion no valida")

# PASS: para defirnir una condiciona que momentaneamene no hace nada.
if edad < 16:
    pass
elif edad >= 16:
    print("Puede conducir")

# NOTA: siver tambien para clases, bucles y funciones 