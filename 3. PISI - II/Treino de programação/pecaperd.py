peças = []

def lista_peças(lista, n):
    '''Função para fazer a lista de peças'''
    # Loop para adicionar N-1 peças na lista
    for i in range(1, n):
        while True:
            num = int(input())
            if 1 <= num <= n:
                break
        # Adiciona o número na lista de peças apenas se ele ainda não tiver sido digitado
        if num not in lista:
            lista.append(num)
    # Retorna a lista de peças ordenada
    return lista.sort()

def peça_faltando(lista):
    '''Função para verificar qual a peça que está faltando'''
    # Loop para verificar a peça em falta
    for i in range(n, 0, -1):
        if i not in lista:
            print(i)
            break

while True:
    n = int(input('Quantidade: '))
    if 2 <= n <= 1000:
        lista_peças(peças, n)
        peça_faltando(peças)
        break
