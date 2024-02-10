medidas = []
for i in range(0, 5):
    while True:
        n = int(input())
        if 1 <= n <= 100:
            medidas.append(n)
            break

# Atribuindo as medidas à variáveis para facilitar a verificação das dimensões
a, b, c, h, l = medidas[0], medidas[1], medidas[2], medidas[3], medidas[4]

# Comparando as dimensões da caixa com as dimensões da janela
if a <= h and a <= l:
    print('S')
elif b <= h and b <= l:
    print('S')
elif c <= h and c <= l:
    print('S')
else:
    print('N')
