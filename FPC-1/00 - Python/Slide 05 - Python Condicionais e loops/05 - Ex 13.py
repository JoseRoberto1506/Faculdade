base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
cont, total = 1, base

while cont <= expoente - 1:
    total *= base
    cont += 1

print(total)
