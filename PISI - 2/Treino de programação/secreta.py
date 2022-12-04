# Loop para pedir o tamanho da sequência até que a restrição seja obedecida
while True:
    n = int(input())
    if 3 <= n <= 500:
        break

sequencia = []
# Adicionando N números da sequência em uma lista
for i in range(n):
    sequencia.append(int(input()))

# Variável para armazenar a quantidade máxima de números que podem ser marcados com um círculo
total = 0
# Variável auxiliar para armazenar se o número anterior foi marcado com um círculo
aux = False

def verificar_sequencia(c, num, lista):
    '''Função para verificar os dois números após o número atual'''
    for j in range(num + 1, num + 3):
        # 'If' para verificar se o 'j' não sai da lista. Se não sair, verifica o número no índice 'j'.
        if j < len(lista):
            if lista[j] != lista[i]:
                break
            else:
                c += 1
    return c

# Para cada número da sequência
for i in range(0, len(sequencia)):
    # Variável para contar quantos números iguais tem em sequência
    cont = 0
    
    if i == 0:
        verificar_sequencia(cont, i, sequencia)
    else:
        if sequencia[i] == sequencia[i-1]:
            if aux == False:
                verificar_sequencia(cont, i, sequencia)
            else:
                continue
        else:
            verificar_sequencia(cont, i, sequencia)

    # Se cont == 0 ou cont == 1, o número pode ser marcado com um círculo
    if cont < 2:
        total += 1
        aux = True
    else:
        aux = False

print(total)

# Se o número atual é igual ao anterior e os dois podem ser circulados, tem que desconsiderar o número atual