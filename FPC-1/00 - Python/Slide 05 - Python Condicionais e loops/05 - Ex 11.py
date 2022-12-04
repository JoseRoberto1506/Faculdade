numero = int(input("Digite um número para calcular seu fatorial: "))
if numero <= 20:
    fat = 1
    for i in range(2, numero+1):
        fat *= i
    print(fat)
else:
    print("Digite um número <= 20")
