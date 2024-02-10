def main():
    texto = """
    Em alguns casos, um aumento na carga tributária de um país pode acabar diminuindo quanto o governo arrecada em impostos. Essa relação, bastante discutida no
    meio econômico, é conhecida como curva de Laffer. A primeira vista, o princípio da curva de Laffer parece não fazer sentido. Se o governo aumenta os impostos,
    o normal seria a arrecadação sempre aumentar também. Porém, o efeito das políticas monetária e fiscal sobre a economia contrariam essa lógica. A curva de Laffer
    é uma definição econômica que mostra quanto o governo arrecada de impostos aplicando diferentes alíquotas. Segundo a curva, essa relação não é diretamente
    proporcional – ou seja, em determinado ponto, um aumento na tributação resultaria em uma receita menor do que antes. Seu conceito foi desenvolvido pelo
    economista Arthur Laffer, que defendia a diminuição dos impostos cobrados em uma sociedade como uma forma de estimular a economia. Com essa medida, uma menor
    tributação resultaria indiretamente em um aumento na arrecadação do Estado. A partir disso, se concluiu que a representação gráfica entre alíquota de impostos
    e receita tributária não seria uma reta ascendente, e sim uma “curva” voltada para baixo – a chamada curva de Laffer.
    """
    mensagem = limpar_texto_deslocamento(texto)
    chave = 15
    texto_cifrado = cifra_deslocamento(mensagem, chave)
    frequencias_texto_original = contar_frequencia(mensagem.upper())
    frequencias_texto_cifrado = contar_frequencia(texto_cifrado)
    i_portugues = 0.073 # constante de idioma do português
    chave_decifrar = encontrar_chave(frequencias_texto_original, frequencias_texto_cifrado, i_portugues)

    print(f'Mensagem:{mensagem}\n')
    print(f'Texto cifrado:{texto_cifrado}\n')
    print(f'Texto decifrado:{cifra_deslocamento(texto_cifrado, chave_decifrar * -1)}')


def limpar_texto_deslocamento(texto):
    texto_limpo = ""

    for c in texto.lower():
        if c == "ç":
            texto_limpo += "c"
        elif c in ["ã", "â", "á", "à"]:
            texto_limpo += "a"
        elif c in ["ê", "é", "è"]:
            texto_limpo += "e"
        elif c in ["î", "í", "ì"]:
            texto_limpo += "i"
        elif c in ["õ", "ô", "ó", "ò"]:
            texto_limpo += "o"
        elif c in ["û", "ú", "ù"]:
            texto_limpo += "u"
        else:
            texto_limpo += c

    return texto_limpo


def cifra_deslocamento(texto, chave):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cifra = ''

    for c in texto:
        if c.isalpha():
            posicao_c = alfabeto.index(c.upper())
            deslocar = (posicao_c + chave) % 26
            cifra += alfabeto[deslocar]
        else:
            cifra += c

    return cifra


def obter_quantidade_letras_do_texto(texto):
    quantidade_letras = 0
    for c in texto:
        if c.isalpha():
            quantidade_letras += 1

    return quantidade_letras


def contar_frequencia(texto):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    total_letras = obter_quantidade_letras_do_texto(texto)
    frequencias = [] # cada elemento é o percentual de ocorrência de cada letra do alfabeto no texto
    for letra in alfabeto:
        frequencias.append(texto.count(letra) / total_letras)

    return frequencias


def encontrar_chave(frequencias_texto_orignial, frequencias_texto_cifrado, i_portugues):
    indices_de_chave = [] # cada elemento da lista é o índice de cada chave, que varia de 1 a 25
    for i in range(1, 26):
        indice_da_chave_i = 0
        for j in range(0, 26):
            indice_da_chave_i += (frequencias_texto_orignial[j] * frequencias_texto_cifrado[(j + i) % 26])
        indices_de_chave.append(indice_da_chave_i)

    # Encontrar o índice de chave mais próximo da constante de idioma do português
    valor_mais_proximo = None
    diferenca_mais_proxima = float('inf')
    for indice in indices_de_chave:
        diferenca = abs(indice - i_portugues)
        if diferenca < diferenca_mais_proxima:
            diferenca_mais_proxima = diferenca
            valor_mais_proximo = indice

    return indices_de_chave.index(valor_mais_proximo) + 1


main()
