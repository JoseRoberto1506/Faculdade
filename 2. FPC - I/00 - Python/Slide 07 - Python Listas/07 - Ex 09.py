notas = []

while True:
    nota = float(input("Digite uma nota (99 para sair): "))
    if nota == 99:
        break
    else:
        notas.append(nota)

quantidade_notas = len(notas)
soma_notas = sum(notas)
media_notas = soma_notas / quantidade_notas

print(f"{quantidade_notas} nota(s) informada(s)")
print(f"Notas: {notas}")

print("Notas informadas em ordem inversa:")
for i in range(-1, quantidade_notas*-1 - 1, -1):
    print(notas[i])

print(f"Soma das notas: {soma_notas}")
print(f"Média das notas: {media_notas:.2f}")

print("Notas acima da média:")
for nota in notas:
    if nota > media_notas:
        print(nota)
