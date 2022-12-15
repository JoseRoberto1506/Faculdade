vitorias = 0

for i in range (6):
    while True:
        # Input do resultado, tratando a string para retirar espaços em branco e colocar a letra em maiúscula
        r = str(input()).strip().upper()
        if r == 'V':
            vitorias += 1
            break
        if r == 'P':
            break

# Imprimindo o grupo do jogador baseado na quantidade de vitórias
if vitorias >= 5:
    print(1)
elif vitorias >= 3:
    print(2)
elif vitorias >= 1:
    print(3)
else:
    print(-1)
