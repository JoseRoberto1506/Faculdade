# Função recursiva para calcular o MDC (Máximo Divisor Comum)
def mdc(x, y):
    if x > y:
        return mdc(x-y, y)
    elif x == y:
        return x
    else:
        return mdc(y, x)

print(mdc(98, 66))
