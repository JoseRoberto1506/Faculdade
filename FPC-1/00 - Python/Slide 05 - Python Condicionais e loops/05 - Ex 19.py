quantidade_pares = quantidade_impares = 0

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        quantidade_pares += 1
    else:
        quantidade_impares += 1

print(f"Ao todo foram digitados {quantidade_pares} números pares e {quantidade_impares} números ímpares")
