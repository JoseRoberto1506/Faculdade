votantes = int(input("Número total de votantes: "))
candidato_1 = candidato_2 = candidato_3 = 0

for i in range(votantes):
    while True:
        voto = int(input("Número do seu candidato (1, 2, 3): "))
        if voto in [1, 2, 3]:
            if voto == 1:
                candidato_1 += 1
            elif voto == 2:
                candidato_2 += 1
            else:
                candidato_3 += 1
            break
        else:
            print("Digite um voto válido")

print(f"O candidato 1 teve {candidato_1} voto(s)")
print(f"O candidato 2 teve {candidato_2} voto(s)")
print(f"O candidato 3 teve {candidato_3} voto(s)")
