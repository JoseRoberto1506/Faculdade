maior_altura = menor_altura = 0
altura_mulheres = quant_mulheres = quant_homens = 0

for i in range(50):
    altura = float(input("Altura em metros: "))
    sexo = str(input("Sexo (M/F): ")).strip().upper()

    if sexo == 'F':
        altura_mulheres += altura
        quant_mulheres += 1
    elif sexo == 'M':
        quant_homens += 1
    
    if i == 0:
        menor_altura = altura
    if altura > maior_altura:
        maior_altura = altura
    elif altura < menor_altura:
        menor_altura = altura

porcent_homens = (quant_homens / 50) * 100
porcent_mulheres = (quant_mulheres / 50) * 100

print(f"A maior altura do grupo é {maior_altura}m, e a menor altura é {menor_altura}m")
print(f"A média de altura das mulheres é de {altura_mulheres/quant_mulheres}")
print(f"Ao todo o grupo tem {quant_homens} homens")
print(f"A quantidade de homens é igual a {porcent_homens}%, e a quantidade de mulheres é igual a {porcent_mulheres}%")
