parametros_iniciales = raw_input()
param_i = parametros_iniciales.split(' ')
h_x = float(param_i[0])
J = float(param_i[1])
k = int(param_i[2])
prob = 0
for i in range(k):
    group = raw_input()
    group_s = group.split(' ')
    g = float(group_s[0])
    h_i = float(group_s[1])
    prob += g * ((h_x) / (h_i + h_x))
prob = prob * (1/J)
print prob