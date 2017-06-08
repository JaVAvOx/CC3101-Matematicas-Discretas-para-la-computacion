k = input()
F = []
G = []
for i in range(101):
    F.append(None)
    G.append(None)

F[0] = 1
G[0] = 2
sum = 0
def f(n):
    global F, G
    if F[n] != None:
        return F[n]
    else:
        F[n] = (5*f(n-1) + 2*g(n-1))%100
        return F[n]

def g(n):
    global F, G
    if G[n] != None:
        return G[n]
    else:
        G[n] = (3*f(n-1) + g(n-1))%100
        return G[n]


def suma(k):
    global sum, G, F
    for i in range(k+1):
        sum += G[i%100] + F[i%100]
    print sum



f(100)
g(100)

suma(k)
