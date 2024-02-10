from random import randint
# Armazenando 'n' números inteiros aleatórios em uma lista
numeros = [randint(1, 10) for _ in range(7)]

# Função recursiva para calcular o maior valor em uma lista
def max(lista):
    if len(lista) == 1:
        return lista[0]
    elif len(lista) == 2:
        if lista[0] > lista[1]:
            return lista[0]
        else:
            return lista[1]
    else:
        return max([max(lista[1:]), lista[0]])

print(numeros)
print(max(numeros))
