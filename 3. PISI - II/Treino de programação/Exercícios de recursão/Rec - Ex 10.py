# Soma recursiva de um array de números reais
def soma_reais(lista, somas):
    # somas = Quantidade de somas a serem feitas
    if somas >= 0:
        return  lista[0] + soma_reais(lista[1:], somas - 1)
    else:
        return 0

reais = [2, 8, 4, 5, 3]
print(soma_reais(reais, len(reais) - 1))
