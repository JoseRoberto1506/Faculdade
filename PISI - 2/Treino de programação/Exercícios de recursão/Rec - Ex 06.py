# Cálculo recursivo de potência ('x' elevado a 'n')
def potencia(x, n):
    # Cálculo de potência com expoente negativo
    if n < 0:
        return 1 / potencia(x, n + (-2*n))
    # Cálculo geral da potência
    elif n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * potencia(x, n-1)

print(potencia(2, 4))
