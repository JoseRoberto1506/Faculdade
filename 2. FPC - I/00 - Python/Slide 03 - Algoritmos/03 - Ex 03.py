soma_idades = quantidade = maior = 0
menor = 200

while True:
    idade = int(input("Digite a idade: "))
    if idade == 0:
        break

    soma_idades += idade
    quantidade += 1

    if idade > maior:
        maior = idade
    elif idade < menor:
        menor = idade

media = soma_idades / quantidade
print(f"A média das idades é: {media}")
print(f"A maior idade é {maior} e a menor idade é {menor}")
