from random import randint
from math import factorial as fat

def sortear(tot_sorteios):
    '''
    Função para realizar todos os sorteios da loteria. 
    A função será chamada recursivamente para fazer novos sorteios até que não haja mais nenhum sorteio possível a ser realizado.
    '''
    global dezenas
    global sorteios_possíveis

    if tot_sorteios >= 1:
        sorteio = []
        for i in range(dezenas):
            while True:
                i = randint(1, 60)
                if i not in sorteio:
                    sorteio.append(i)
                    break
        sorteios_possíveis.append(sorteio)
    return sortear(tot_sorteios - 1)

# Lista para armazenar todos os sorteios possíveis
sorteios_possíveis = []
dezenas = int(input("Quantidade de dezenas: "))
# Calculando a quantidade de sorteios possíveis
quant_resultados = int(fat(60) / (fat(dezenas) * fat(60 - dezenas)))

# print(sortear(dezenas))
# print(quant_resultados)
