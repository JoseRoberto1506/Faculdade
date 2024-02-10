# Cálculo recursivo da raiz quadrada de um número real
def raiz_Q(x, y, e):
    if pow(y, 2) - x <= e:
        return y
    else:
        return raiz_Q(x, ((pow(y, 2) + x) / 2*y), e)

print(raiz_Q(13, 3.2, 0.001))
