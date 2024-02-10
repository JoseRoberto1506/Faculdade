total = 1
while total <= 5:
    numero = int(input("Digite um número postivo: "))
    if numero < 0:
        break
    total += 1
else:
    print("Os dados foram inseridos com sucesso")
