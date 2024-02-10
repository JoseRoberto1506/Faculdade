maior_altura = menor_altura = 0
altura_mulheres = quant_mulheres = quant_homens = 0
sexo_pessoa_mais_alta = []

for i in range(15):
    altura = float(input("Altura em metros: "))
    sexo = str(input("Sexo (M/F): ")).strip().upper()

    if sexo == 'F':
        altura_mulheres += altura
        quant_mulheres += 1
    elif sexo == 'M':
        quant_homens += 1
    
    if i == 0:
        maior_altura = menor_altura = altura
        sexo_pessoa_mais_alta.append(sexo)
    else:
        if altura > maior_altura:
            maior_altura = altura
            sexo_pessoa_mais_alta.append(sexo)
        elif altura < menor_altura:
            menor_altura = altura

print(f"A maior altura do grupo é {maior_altura}m, e a menor altura é {menor_altura}m")
print(f"A média de altura das mulheres é de {altura_mulheres/quant_mulheres:.2f}m")
print(f"Ao todo o grupo tem {quant_homens} homens")
print(f"A pessoa mais alta é do sexo {sexo_pessoa_mais_alta[-1]}")
