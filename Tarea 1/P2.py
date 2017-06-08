letras = ['A', 'B', 'C']
def rn(n, d1, d2):  # Movemos n discos de d1 a d2, las que son dos torres en orden inverso (ej. d1 = C y d2 = A
                    # movimiento que no esta permitido, por lo que debemos 'mover dos veces hacia adelante'
    # Casos base primero
    if n == 0:
        print ''
    elif n == 1:
        # Con uno solo disco, debemos moverlo dos veces (por las reglas del problema)
        print letras[d1%3] + ' -> ' + letras[(d1 + 1)%3]
        print letras[(d1 + 1)%3] + ' -> ' + letras[(d1 + 2)%3]
    else:
        # Movemos n-1 discos de d1 a d2 recursivamente
        rn(n - 1, d1, d2)
        # Movemos el disco restante de d1 a d1+1 (lo que sera la siguiente torre, es decir, si estamos en A, sera B,
        # o si estamos en B sera C)
        print letras[d1%3] + ' -> ' + letras[(d1 + 1)%3]
        # Movemos n-1 discos de d1+1 a d1+2 (es decir, una torre hacia adelante)
        qn(n - 1, d1 - 1, d1)
        # Movemos el disco faltante una torre hacia adelante
        print letras[(d1 + 1)%3] + ' -> ' + letras[(d1 + 2)%3]
        # Movemos los n-1 discos de d1 a d2 recursivamente
        rn(n - 1, d1, d2)


def qn(n, d1, d2):  # Movemos n discos 'hacia adelante' desde d1 a d2, las que deben estar en orden
                    # (por ejemplo, A y B, o C y A, nunca mover para 'atras' ya que no esta permitido)
    # Casos base primero
    if n == 0:
        print ''
    elif n == 1:
        print letras[d1%3] + ' -> ' + letras[d2%3]
    else:
        # Movemos n-1 discos pero cambiamos el destino (-1 indica que retrodecemos una letra, es decir, si
        # estabamos en B ahora estaremos en A
        rn(n - 1, d1, d1 - 1)
        # Movemos el n-esimo disco solo (ver pdf)
        print letras[d1%3] + ' -> ' + letras[d2%3]
        # Movemos los n-1 discos que habiamos movido a la letra que nos faltaba (es decir, la que no
        # correspondia ni a d1 ni a d2 originales)
        rn(n - 1, d1 - 1, d1 - 2)


n = input()
qn(n, 0, 1)  # 0 y 1 corresponden a A y B respectivamente, origen y destino de donde queremos nuestra torre
