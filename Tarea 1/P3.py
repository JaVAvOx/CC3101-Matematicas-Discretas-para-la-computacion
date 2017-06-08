import random
input_lista = raw_input().split(",")  # la lista ingresa como un string
lista = []  # creamos una lista para guardar los elementos como enteros (no string)
for i in range(len(input_lista)):
    lista.append(int(input_lista[i]))
largo = len(lista)
resultado = 0  # caso de lista vacia
for i in range(largo):
    p = random.randint(1, i+1)
    if p == (i + 1) :
        resultado = lista[i]
print resultado