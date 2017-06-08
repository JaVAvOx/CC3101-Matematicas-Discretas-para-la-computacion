d = input()
def contar(d):
    no_posible = [0, 1, 2, 4, 7]
    base = [3, 5, 6, 9, 10]
    suma= 0
    if no_posible.count(d) == 1 or d < 0:
        suma += 0
    else:
        if base.count(d) >= 1:
            suma += 1
        elif d == 8:
            suma += 2
        elif d == 11:
            suma += 3
        else:
            suma += (contar(d-3) + contar(d-5))
    return suma

a = contar(d)
print a