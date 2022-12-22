# Função recursiva para calcular o resto da divisão (MOD)
def mod(x, y):
    if x > y:
        return mod(x-y, y)
    elif x < y:
        return x
    else:
        return 0

print(mod(5, 3))
