def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)


def binomio(x,y):
    res = float(factorial(x)) / (factorial(x-y) * factorial(y))
    return res



parametros_d = raw_input()
param_d = parametros_d.split(' ')
n = int(param_d[0])
m = int(param_d[1])

parametros = raw_input()
param_i = parametros.split(' ')
h_x = float(param_i[0])
J = float(param_i[1])
k = int(param_i[2])
p = 0
for i in range(k):
    group = raw_input()
    group_s = group.split(' ')
    g = float(group_s[0])
    h_i = float(group_s[1])
    p += g * ((h_x) / (h_i + h_x))
p = p * (1/J)

prob_ganar = 0

prob_ganar += p**n # sumamos la probabilidad de que gane n seguidas al comienzo

# realizamos la sumatoria

for i in range(n+1, m):
    if 2*i - n <= m:
        prob_ganar += (p**i) * ((1-p)**(i-n)) * (binomio((2*i) - n, i) - binomio(2*(i-n), i-n))

    else:
        pass


print prob_ganar