numeros = []
for i in range(3):
    numeros.append(int(input("Digite um número: ")))
numeros.sort(reverse=True)
for n in numeros:
    print(n)
