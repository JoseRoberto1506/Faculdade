total = 0
while True:
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura (m): "))

    if altura == 0:
        break
    if idade > 13 and altura < 1.5:
        total += 1

print(f"{total} alunos tem mais de 13 anos e altura inferior a 1.5m")
