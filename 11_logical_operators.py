"""  OPERADORES LOGICOS  """

"""  VALORES QUE PYTHON INTERPRETA COMO FALSE:
  · False
  · None
  · 0 (cero)
  · 0.0
  · "" (cadena vacía)
  · [] (lista vacía)
  · {} (diccionario vacío)
  · () (tupla vacía)
Todo lo demás se interpreta como True.
"""
# AND
bool_1= "a"
bool_2= ""
print(f"{bool(bool_1) and bool(bool_2)}")

# OR
print(f"{bool(bool_1) or bool(bool_2)}")

# NOT
print(f"{bool(bool_1)}")
print(f"{not bool(bool_1)}")