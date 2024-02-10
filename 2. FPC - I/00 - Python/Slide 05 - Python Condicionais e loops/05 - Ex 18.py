print("-" * 25)
print(f"{'MENU DE VOTOS':^25}")
print("-" * 25)
print('''[ 1 ] - Candidato A
[ 2 ] - Candidato B
[ 3 ] - Candidato C
[ 4 ] - Voto nulo
[ 5 ] - Voto em branco''')
print("-" * 25)

candidato_a = candidato_b = candidato_c = voto_nulo = voto_branco = 0

for i in range(1, 16):
    while True:
        voto = int(input(f"Voto {i}: "))
        if voto in [1, 2, 3, 4, 5]:
            if voto == 1:
                candidato_a += 1
            elif voto == 2:
                candidato_b += 1
            elif voto == 3:
                candidato_c += 1
            elif voto == 4:
                voto_nulo += 1
            else:
                voto_branco += 1
            break
        else:
            print("Digite um voto válido")

porcent_votos_nulos = (voto_nulo / 15) * 100
porcent_votos_brancos = (voto_branco / 15) * 100

print(f'''Candidato A: {candidato_a} voto(s)
Candidato B: {candidato_b} voto(s)
Candidato C: {candidato_c} voto(s)''')

print(f'''Votos nulos: {voto_nulo} voto(s)
Votos brancos: {voto_branco} voto(s)''')

print(f"Porcentagem de votos nulos: {porcent_votos_nulos:.2f}%")
print(f"porcentagem de votos brancos: {porcent_votos_brancos:.2f}%")
