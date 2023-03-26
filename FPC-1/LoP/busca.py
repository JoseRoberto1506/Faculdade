def main():
    lista_numeros = [int(i) for i in input().split()]
    # Número buscado | Lista de números | Quantidade de comparações
    print(busca_binaria(lista_numeros[0], lista_numeros[1:], 0))


def busca_binaria(num, lista, comps):
    from math import floor
    
    # Caso base
    if len(lista) == 0:
        return comps
    else:
        comps += 1
    
    # Identificar o elemento central
    if len(lista) % 2 == 0:
        meio = len(lista) // 2
    else:
        meio = floor(len(lista) / 2)
    
    if lista[meio] == num: # Número encontrado
        return comps
    elif num > lista[meio]: # Número está no lado direito da lista
        return busca_binaria(num, lista[meio + 1:], comps)
    elif num < lista[meio]: # Número está do lado esquerdo da lista
        return busca_binaria(num, lista[:meio], comps)


main()
