'''
Dados do artigo para o Algoritmo Genético:

- Representação (codificação) da população: Ponto flutuante;
- Cromossomo: Portfolio (cesta de ações);
- Gene: Pesos atribuídos à cada ação no portfolio;
    - Os genes são formados atribuindo valores aleatórios de acordo com a distribuição de probabilidade normal;
    - Valores aleatórios (V_i) são usados para calcualr pesos (w_i) da ação selecionada, ou seja, V_i/∑V_i;
- Função de aptidão: max(Retorno do portfolio / Risco do Portfolio)
- Função de seleção: f(i evaluation) = f(chromossome i) / ∑f(chromossome i)
- Seleção de pais e sobreviventes: Roleta;
- Tamanho da população (N): 10 cromossomos
- Operador de cruzamento: Crossover aritmético
    - Offspring 1 = alpha * CH1 + (1+alpha) * CH2
    - Offspring 2 = (1-alpha) * CH1 + alpha * CH2
    - CH1 e CH2: pais;
- Probabilidade de crossover: 0.6
- Operador de mutação: 
- Probabilidade de mutação: 0.4;
- Quantidade de gerações: 100;
- O artigo selecina 4 ações, e então o AG otimiza os pesos.
'''

from typing import List
import json
import numpy as np
import pandas as pd
from random import uniform, random, randint


def carregar_dados_json(path: str) -> pd.DataFrame:
    """
    Carrega os dados das empresas a partir de um arquivo JSON e retorna um DataFrame do Pandas.
    O aritgo não especificou o formato do arquivo de entrada, então optei por criar um JSON.
    """
    with open(path, 'r') as f:
        data = json.load(f)
    print(pd.DataFrame(data))

    return pd.DataFrame(data)


def gerar_cromossomo(n_acoes: int) -> List[float]:
    """
    Cria uma lista com o peso de cada ação no portfolio (cromossomo).
    """
    pesos = np.random.rand(n_acoes)
    return (pesos / pesos.sum()).tolist()


def gerar_populacao(n_acoes: int, tamanho_pop: int) -> List[List[float]]:
    """
    Gera uma população inicial de cromossomos (portfólios).
    """
    return [gerar_cromossomo(n_acoes) for _ in range(tamanho_pop)]


def calcular_aptidao_individuo(individuo: List[float], retornos: pd.DataFrame, riscos: pd.DataFrame) -> float:
    """
    Calcula a aptidão de um cromossomo (portfólio).
    O artigo não explicou como encontrou a covariância entre as ações, então calculei a aptidão sem ela.
    """
    individuo: pd.DataFrame = np.array(individuo)
    retornos: pd.DataFrame = np.array(retornos)
    riscos: pd.DataFrame = np.array(riscos)

    retorno_portfolio: float = np.dot(individuo, retornos)
    risco_portfolio: float = np.sum((individuo ** 2) * (riscos ** 2))
    aptidao: float = retorno_portfolio / risco_portfolio

    return aptidao


def selecao_por_roleta(pop: List[List[float]], aptidoes: List[float]) -> List[List[float]]:
    """
    Seleciona indivíduos da população com base na aptidão.
    A probabilidade de seleção é proporcional à aptidão.
    """
    total_aptidao = sum(aptidoes)
    probabilidades = [aptidao / total_aptidao for aptidao in aptidoes]
    indices = np.random.choice(len(pop), size=len(pop), p=probabilidades)
    
    return [pop[i] for i in indices]


def crossover_aritmetico(pais: List[List[float]], taxa_crossover: float) -> List[List[float]]:
    """
    Realiza o crossover aritmético entre dois pais.
    O artigo não especificou o alpha utilizado, então utilizei um valor aleatório entre 0 e 1.
        - Offspring 1 = alpha * CH1 + (1+alpha) * CH2
        - Offspring 2 = (1-alpha) * CH1 + alpha * CH2
        - CH1 e CH2 são pais.
    """
    lista_filhos: List[List[float]] = []
    n_pais: int = len(pais)

    for i in range(0, n_pais, 2):
        pai_1: List[float] = pais[i]
        pai_2: List[float] = pais[i+1]

        if random() <= taxa_crossover:
            alpha: float = uniform(0, 1)
            filho_1: List[float] = [alpha * ch1 + (1 - alpha) * ch2 for ch1, ch2 in zip(pai_1, pai_2)]
            filho_2: List[float] = [(1 - alpha) * ch1 + alpha * ch2 for ch1, ch2 in zip(pai_1, pai_2)]
        else:
            filho_1 = pai_1[:]
            filho_2 = pai_2[:]

        filho_1 = [gene / sum(filho_1) for gene in filho_1]
        filho_2 = [gene / sum(filho_2) for gene in filho_2]
        lista_filhos.extend([filho_1, filho_2])

    return lista_filhos
   

def mutacao_permutacao_gaussiana(filhos: List[List[float]], taxa_mutacao: float) -> List[List[float]]:
    """
    Aplica a mutação nos cromossomos (portfolios).
    O artigo não especificou o operador de mutação utilizado, então usei a mutação por Perturbação Gaussiana.
    Para cada cromossomo, escolho um gene aleatório e aplico uma perturbação gaussiana.
    """
    MEDIA: int = 0
    DESVIO: float = 0.05

    for cromossomo in filhos:
        if random() <= taxa_mutacao:
            index_gene_escolhido = randint(0, len(cromossomo) - 1)
            perturbacao = np.random.normal(MEDIA, DESVIO)
            cromossomo[index_gene_escolhido] += perturbacao
            cromossomo[index_gene_escolhido] = max(cromossomo[index_gene_escolhido], 0)
            cromossomo = [gene / sum(cromossomo) for gene in cromossomo]

    return filhos


def algoritmo_genetico(df: pd.DataFrame) -> List[float]:
    TAM_POP: int = 10
    GERACOES: int = 1000
    TAXA_CROSSOVER: float = 0.6
    TAXA_MUTACAO: float = 0.4

    n_acoes: int = len(df)
    pop: List[List[float]] = gerar_populacao(n_acoes, TAM_POP)

    for geracao in range(GERACOES):
        aptidoes: List[float] = [calcular_aptidao_individuo(individuo, df['Retorno'], df['Risco']) for individuo in pop]
        pais: List[List[float]] = selecao_por_roleta(pop, aptidoes)
        filhos: List[List[float]] = crossover_aritmetico(pais, TAXA_CROSSOVER)
        filhos: List[List[float]] = mutacao_permutacao_gaussiana(filhos, TAXA_MUTACAO)
        pop = filhos[:TAM_POP]
        # melhor_aptidao = max(aptidoes)
        # print(f"Geração {geracao + 1}: melhor aptidão = {melhor_aptidao:.4f}")

    aptidoes = [calcular_aptidao_individuo(individuo, df['Retorno'], df['Risco']) for individuo in pop]

    return pop[np.argmax(aptidoes)]


if __name__ == "__main__":
    df = carregar_dados_json('acoes.json')
    melhor_portfolio = algoritmo_genetico(df)
    portfolio_final = df[['Ticker']].copy()
    portfolio_final['Peso'] = melhor_portfolio
    portfolio_final['Peso (%)'] = (portfolio_final['Peso'] * 100).round(2)

    print("\nPortfólio ótimo encontrado (pesos):")
    print(portfolio_final)
