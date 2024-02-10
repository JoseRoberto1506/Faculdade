matriz = []
linhas = int(input("Quantas linhas a matriz terá? "))
colunas = int(input("Quantas colunas a matriz terá? "))

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor da posição ({i}, {j}): "))
        linha.append(valor)
    matriz.append(linha)

for elemento in matriz:
    print(elemento)
