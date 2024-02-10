# Calcular recursivamente quantas vezes um dígito 'k' ocorre em um número 'n'
def quantidade(cont, k, n):
    # cont = Quantidade de dígitos a serem verificados
    if cont > 0:
        if k == n[0]:
            return 1 + quantidade(cont - 1, k, n[1:])
        else:
            return quantidade(cont - 1, k, n[1:])
    else:
        return 0

numero = '762021192'
print(quantidade(len(numero), str(2), numero))
