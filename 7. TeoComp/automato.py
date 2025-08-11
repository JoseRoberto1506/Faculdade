import json
from collections import defaultdict

class Automato:
    def __init__(self, tipo, alfabeto, estados, inicial, finais, transicoes):
        self.tipo = tipo  # "AFD" ou "AFND"
        self.alfabeto = alfabeto
        self.estados = estados
        self.inicial = inicial
        self.finais = finais
        self.transicoes = transicoes

    def salvar(self, nome_arquivo):
        with open(nome_arquivo, 'w') as f:
            json.dump(self.__dict__, f, indent=2)

    @staticmethod
    def carregar(nome_arquivo):
        with open(nome_arquivo, 'r') as f:
            data = json.load(f)
            return Automato(**data)

    def __repr__(self):
        return f"<{self.tipo} com {len(self.estados)} estados>"


def determinizar(afnd: Automato) -> Automato:
    assert afnd.tipo == "AFND", "Somente AFNDs podem ser determinizados."

    inicial = frozenset([afnd.inicial])
    fila = [inicial]
    visitados = set()
    transicoes_deterministas = {}
    novos_finais = set()
    mapeamento_nomes = {inicial: "Q0"}
    contador = 1

    while fila:
        estado_atual = fila.pop()
        if estado_atual in visitados:
            continue
        visitados.add(estado_atual)

        nome_atual = mapeamento_nomes[estado_atual]
        transicoes_deterministas[nome_atual] = {}

        for simbolo in afnd.alfabeto:
            destino = set()
            for estado in estado_atual:
                if estado in afnd.transicoes and simbolo in afnd.transicoes[estado]:
                    destino.update(afnd.transicoes[estado][simbolo])
            destino_frozen = frozenset(destino)

            if destino_frozen not in mapeamento_nomes and destino:
                mapeamento_nomes[destino_frozen] = f"Q{contador}"
                contador += 1
                fila.append(destino_frozen)

            if destino:
                transicoes_deterministas[nome_atual][simbolo] = mapeamento_nomes[destino_frozen]

        if any(e in afnd.finais for e in estado_atual):
            novos_finais.add(nome_atual)

    return Automato(
        tipo="AFD",
        alfabeto=afnd.alfabeto,
        estados=list(mapeamento_nomes.values()),
        inicial="Q0",
        finais=list(novos_finais),
        transicoes=transicoes_deterministas
    )
