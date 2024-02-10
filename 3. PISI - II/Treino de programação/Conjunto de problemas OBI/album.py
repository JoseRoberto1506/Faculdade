# Input para o total de figurinhas e espaços no álbum
while True:
    total = int(input())
    if 1 <= total <= 100:
        break
# Input para o número de figurinhas compradas
while True:
    compradas = int(input())
    if 1 <= compradas <= 300:
        break

# Lista com as figurinhas compradas, desconsiderando as repetidas
figurinhas = []
for i in range(0, compradas):
    n = int(input())
    # Adicionar novas figurinhas na lista
    if n not in figurinhas:
        figurinhas.append(n)

print(total - len(figurinhas))
