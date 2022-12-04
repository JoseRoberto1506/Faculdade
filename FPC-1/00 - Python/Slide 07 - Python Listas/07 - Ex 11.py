def header():
    print("-" * 59)
    print(f"{'Qual o melhor sistema operacional para uso em servidores?':^60}")
    print("-" * 59)
    print('''    [ 1 ] - Windows XP
    [ 2 ] - Unix
    [ 3 ] - Linux
    [ 4 ] - Netware
    [ 5 ] - Mac OS
    [ 6 ] - Outro''')
    print("-" * 59)

header()
respostas = []
total_votos = 0
opções = ["Windows XP", "Unix", "Linux", "Netware", "Mac OS", "Outro"]

while True:
    voto = int(input("Digite a sua opção: "))
    if voto == 0:
        print()
        break
    elif (voto < 0) or (voto > 6):
        print("Digite uma opção válida")
        continue
    else:
        respostas.append(voto)
        total_votos += 1

# Quantidade de votos de cada sistema operacional
quantidade_votos = [respostas.count(i) for i in range(1, 7)]
# Percentual de votos de cada sistema operacional
percentual = [(quantidade_votos[i]/total_votos)*100 for i in range(len(quantidade_votos))]
# Index do sistema operacional mais votado
index_mais_votado = quantidade_votos.index(max(quantidade_votos))

print("Sistemas Operacionais | votos | %")
for i in range(6):
    print(f"  {opções[i]:<12} | {quantidade_votos[i]} votos | {percentual[i]:.2f}%")
print(f"Total de {total_votos} votos")
print(f"O sistema operacional mais votado foi o {opções[index_mais_votado]}, com {max(quantidade_votos)} votos, correspondendo a {percentual[index_mais_votado]:.2f}% dos votos")
