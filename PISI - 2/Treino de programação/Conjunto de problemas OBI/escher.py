# Loop para pedir a quantidade de números na sequência até que a restrição seja obedecida
while True:
    n = int(input())
    if 3 <= n <= 10000:
        break

numeros = [int(i) for i in input().split()]

# Se a quantidade de números na sequência for ímpar, não tem como o perfil ser Escher
if n % 2 != 0:
    print("N")
# Se a quantidade de números na sequência for par, há a possibilidade do perfil ser Escher
else:
    j = n - 1 # índice máximo da lista
    metade_n = int(n/2) # Metade da lista
    soma = numeros[0] + numeros[-1] # Soma do primeiro número com o último
    # Variável para armazenar a quantidade de números em que sua soma com o número correspondente da
    # outra metade é igual à soma do primeiro número com o último
    cont = 1 
    
    # Loop para iterar metade da lista e comparar com a outra metade
    for i in range(1, metade_n):
        if numeros[i] + numeros[j-i] == soma:
            cont += 1
        else:
            break
    if cont == metade_n:
        print("S")
    else:
        print("N")
