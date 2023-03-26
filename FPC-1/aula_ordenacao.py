def gerar_lista():
    from random import randint
    lista_numeros = [randint(1, 30) for i in range(16)]
    print(f'Lista gerada: {lista_numeros}')

    return lista_numeros


def bubble_sort(): # (n²)
    print('-' * 40)
    print(f'{"Bubble Sort":^40}')
    print('-' * 40)

    lista = gerar_lista()
    n = len(lista)
    troca = True
    while troca:
        troca = False
        for i in range(n - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                troca = True
    
    return lista


def insertion_sort(): # O(n²)
    print('-' * 40)
    print(f'{"Insertion Sort":^40}')
    print('-' * 40)

    lista = gerar_lista()
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i
        while j > 0 and lista[j - 1] > chave:
            lista[j] = lista[j - 1]
            j -= 1
        lista[j] = chave
    
    return lista


def shell_sort(): # O(n²)
    print('-' * 40)
    print(f'{"Shell Sort":^40}')
    print('-' * 40)

    lista = gerar_lista()
    n = len(lista)
    h = int(len(lista) / 2)
    while h > 0:
        for i in range(h, n):
            c = lista[i]
            j = i
            while j >= h and c < lista[j - h]:
                lista[j] = lista[j - h]
                j -= h
            lista[j] = c
        h = int(h / 2.2)
    
    return lista


def selection_sort(): # O(n²)
    print('-' * 40)
    print(f'{"Selection Sort":^40}')
    print('-' * 40)

    lista = gerar_lista()
    n = len(lista)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    
    return lista


def quick_sort(lista): # O(n log(n))
    if len(lista) <= 1:
        return lista

    menor, igual, maior = [], [], []
    pivo = lista[0]

    for x in lista:
        if x < pivo:
            menor.append(x)
        elif x == pivo:
            igual.append(x)
        else:
            maior.append(x)
    
    return quick_sort(menor) + igual + quick_sort(maior)


print(f'Lista ordenada: {bubble_sort()}\n')
print(f'Lista ordenada: {insertion_sort()}\n')
print(f'Lista ordenada: {shell_sort()}\n')
print(f'Lista ordenada: {selection_sort()}\n')
print('-' * 40)
print(f'{"Quick Sort":^40}')
print('-' * 40)
print(f'Lista ordenada: {quick_sort(gerar_lista())}')
