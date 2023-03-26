# Imprimir as possíveis sucessões de gols marcados em um jogo de futebol de forma recursiva
def possíveis_sucessões(a, b, total, possibilidades):
    # A quantidade de possíveis sucessões é igual a quantidade de gols no jogo
    if total > 0:
        sucessão = [] # Lista para armazenar uma sucessão de gols
        
        possibilidades.append(sucessão)
        return possíveis_sucessões(a, b, total - 1, possibilidades)
    else:
        return possibilidades

gols_time_1, gols_time_2, sucessões = 0, 3, []
gols = gols_time_1 + gols_time_2
possíveis_sucessões(gols_time_1, gols_time_2, gols, sucessões)

for sucessão in sucessões:
    for gol in sucessão:
        print(gol, end=' ')
    print()
