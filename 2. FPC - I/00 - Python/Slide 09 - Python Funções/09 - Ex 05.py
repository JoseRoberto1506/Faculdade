def mdc(a, b):
    # Assegurar que a >= b
    if a < b:
        a, b = b, a
    # Caso base
    if b == 0:
        return a
    # Cálculo recursivo
    else:
        return mdc(b, a % b)

print(mdc(98, 66))
