"""  CONCATENAR EN PYTHON  """
nombre= "Guillermo"
edad= 25

# COMA ( , ): no concatena, solo muestra varios parametros.
print("nombre:", nombre, "- Edad:", edad)

# SIGNO DE MAS ( + )
print("nombre: "+ nombre+ " - Edad: "+ str(edad))

# .FORMAT()
print("nombre: {} - Edad: {}".format(nombre, edad))

# F-STRING: forma mas moderna y recomendada.
print(f"nombre: {nombre} - Edad: {edad}")