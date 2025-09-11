"""    CONVERTIR TIPO DE DATO
  · int()   -->	 Convierte a número entero
  · float() -->  Convierte a número decimal
  · str()   -->  Convierte a cadena de texto
  · bool()  -->	 Convierte a booleano (0, 0.0, None, "")= False
  · list()  -->	 Convierte a lista
  · tuple() -->  Convierte a tupla
  · set()   -->	 Convierte a conjunto

    EJEMPLOS:
"""
entero= 1

print(type(str(entero)), str(entero))
print(type(float(entero)), float(entero))
print(type(bool(entero)), bool(entero))

tupla= ("A", "B", 1, 2)
print(type(list(tupla)), list(tupla))
print(type(set(tupla)), set(tupla))

"""  REASIGNANDO VARIABLES  """
cadena= "17"
print(type(cadena))

cadena= int(cadena)
print(type(cadena))