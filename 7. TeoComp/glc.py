def afd_para_glc(afd: dict) -> None:
    """
    A primeira conversão consiste em construir uma GLC (gramática livre de contexto) a partir de um autômato determinístico.
    """
    regras = []

    for (estado, simbolo), destino in afd['transições'].items():
        regras.append(f"{estado} -> {simbolo} {destino}")
    
    for final in afd['F']:
        regras.append(f"{final} -> ε")

    glc: dict = {
        'variaveis': afd['estados'],
        'terminais': afd['entrada'],
        'regras': regras,
        'simbolo_inicial': afd['q0']
    }

    print("\nGramática equivalente à AFD:")
    for regra in glc['regras']:
        print(regra)


def glc_para_ap(glc: dict) -> None:
    """
    A segunda conversão transforma uma GLC em um autômato com pilha.
    """
    estado = 'q'
    transições = {}

    for (A, alpha) in glc['regras']:
        chave = (estado, '', A)
        transições[chave] = transições.get(chave, []) + [(estado, alpha)]

    for a in glc['terminais']:
        chave = (estado, a, a)
        transições[chave] = [(estado, '')]

    ap: dict = {
        'estados': {estado},
        'entrada': glc['terminais'],
        'alfabeto': glc['variaveis'].union(glc['terminais']),
        'transições': transições,
        'q0': estado,
        'Z0': glc['simbolo_inicial'],
        'F': set()
    }

    print("\nTransições do AP equivalente à GLC:")
    for chave, destinos in ap['transições'].items():
        for destino in destinos:
            print(f"δ{chave} -> {destino}")


if __name__ == "__main__":
    afd: dict = {
        'estados': {'q0', 'q1'},
        'entrada': {'a'},
        'q0': 'q0',
        'F': {'q0'},
        'transições': {
            ('q0', 'a'): 'q1',
            ('q1', 'a'): 'q0',
        }
    }
    afd_para_glc(afd)
    
    glc: dict = {
        'variaveis': {'S'},
        'terminais': {'a', 'b'},
        'regras': [
            ('S', 'aSb'),
            ('S', '')
        ],
        'simbolo_inicial': 'S',
    }
    glc_para_ap(glc)
