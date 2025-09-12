"""  ESTRUCTURAS REPETITIVAS  """
# WHILE
cont= 1

while cont <= 3:
    print(f"interacion #{cont}.")
    cont+= 1
print("\n")

# FOR RANGE
for i in range(0, 6, 2): # range(inicio, fin, paso)
    print(f"iteracion #{i}.")
print("\n")

for i in range(3):
    print(f"iteracion #{i+1}.")
print("\n")

# RECORRER LISTA
frutas= ["pera", "manzana", "uva"]

for fruta in frutas:
    print(fruta)
print("\n")

for e in range(len(frutas)):
    print(e)
print("\n")

# BREAK: finaliza el bucle automaticamente
indice= 0
while indice < 5:
    if indice == 3:
        break
    print(indice)
    indice+=1
print("\n")

# CONTINUE: salta a la siguiente interaccion
for x in range(1, 5):
    if i == 3:
        continue
    print(x)