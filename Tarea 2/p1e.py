k = input()
args = raw_input()
args2 = args.split(' ')
a = int(args2[0])
b = int(args2[1])
c = int(args2[2])
d = int(args2[3])
m = int(args2[4])
l = int(args2[5])

F = dict()
G = dict()
F[0] = 1
G[0] = 2
sum = 0

def f(n):
    global F, G, a, b, c, d, m, l
    if n == 0:
        return F[0]
    elif n in F:
        return F[n]
    else:
        if ((n-1) in F) and ((n-1) in G):
            F[n] = (a*F[(n-1)] + b*G[(n-1)])%m
            return F[n]
        else:
            F[n] = (a*f((n-1)) + b*g((n-1)))%m
            return F[n]

def g(n):
    global F, G, a, b, c, d, m, l
    if n == 0:
        return G[0]
    elif n in G:
        return G[n]
    else:
        if ((n-1) in F) and ((n-1) in G):
            G[n] = (c*F[(n-1)] + d*G[(n-1)])%l
            return G[n]
        else:
            G[n] = (c*f((n-1)) + d*g((n-1)))%l
            return G[n]


def suma(k):
    global F,G, a, b, c, d, l, m, sum
    for i in range(k+1):
        sum += f(i)+g(i)
    return sum%(10**9 + 7)


print suma(k)