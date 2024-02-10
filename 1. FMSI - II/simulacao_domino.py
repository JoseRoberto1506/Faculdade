def main():
    pecas_deixadas = gerar_pecas_deixadas()
    partidas = 10000
    print([jogar_peca(pecas_deixadas, partidas) for _ in range(10)])


def gerar_pecas_deixadas():
    from random import randint

    peca_1 = randint(0, 5)
    peca_2 = peca_1
    # As duas peças deixadas devem ser diferentes
    while peca_2 == peca_1:
        peca_2 = randint(0, 5)

    return [peca_1, peca_2]


def jogar_peca(pecas, tot_partidas):
    from random import randint
    
    # Quantidade de partidas em que o jogador teve pelo menos uma das duas peças deixadas
    contador = 0
    for _ in range(tot_partidas):
        # Gerar peças do quarto jogador
        pecas_jogador = [randint(0, 5) for _ in range(6)]
        # Se o jogador tiver qualquer uma das peças deixadas, o contador será incrementado
        if (pecas[0] in pecas_jogador) or (pecas[1] in pecas_jogador):
            contador += 1
        
    # Cálculo da probabilidade
    return round(100 * contador / tot_partidas, 2)


main()