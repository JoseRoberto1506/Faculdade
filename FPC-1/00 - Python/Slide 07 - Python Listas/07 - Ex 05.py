from random import randint
numeros = [randint(1, 101) for i in range(20)]
pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print(numeros)
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
