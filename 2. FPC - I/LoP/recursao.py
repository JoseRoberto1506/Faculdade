def potencia(a, b):
    # Caso base para expoente = 0
    if b == 0:
        return 1
    # Caso base para expoente = 1
    elif b == 1:
        return a
    # Passo recursivo
    else:
        return a * potencia(a, b - 1)


base, expoente = [int(i) for i in input().split()]
print(potencia(base, expoente))
