# Função para calcular uma multiplicação de forma recursiva
def multiplicação(x, n):
    if n >= 1:
        return x + multiplicação(x, n-1)
    else:
        return 0

print(multiplicação(2, 5))
