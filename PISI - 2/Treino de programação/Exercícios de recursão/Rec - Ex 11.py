# Inverter a posição dos elementos de um array de forma recursiva
def inverter(lista, c=0, i=-1):
    # c = Quantidade de troca de posições a serem feitas
    if c < (len(lista) / 2):
        aux = lista[c]
        lista[c] = lista[i]
        lista[i] = aux
        return inverter(lista, c+1, i-1)
    else:
        return lista

numeros = [1, 2, 3, 4, 5]
print(inverter(numeros, 0, -1))
