from random import randint

matriz = []
linhas = int(input("Quantas linhas a matriz terá? "))
colunas = int(input("Quantas colunas a matriz terá? "))

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(randint(0, 10))
    matriz.append(linha)

for elemento in matriz:
    print(elemento)
