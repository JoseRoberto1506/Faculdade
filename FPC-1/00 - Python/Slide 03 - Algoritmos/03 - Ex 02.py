soma_notas = 0
for i in range(3):
    nota = float(input("Nota: "))
    soma_notas += nota

media = soma_notas / 3
if media == 10:
    print("Aprovado com louvor")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
