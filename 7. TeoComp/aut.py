import collections

# 1. Classe para representar Autômatos Finitos Não-Determinísticos (AFNDs)
#    Esta classe pode representar AFDs também, já que um AFD é um caso especial de AFND.
class AFND:
    """
    Representa um Autômato Finito Não-Determinístico (AFND).
    Um AFD é um caso especial onde cada transição leva a um único estado.
    """
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_finais):
        """
        Inicializa um objeto AFND.

        Args:
            estados (set): Um conjunto de strings ou inteiros representando os estados do autômato.
            alfabeto (set): Um conjunto de strings representando os símbolos do alfabeto de entrada.
            transicoes (dict): Um dicionário aninhado que representa a função de transição.
                               Formato: {estado_origem: {simbolo: {estado_destino_1, estado_destino_2, ...}}}
            estado_inicial (str/int): O estado inicial do autômato.
            estados_finais (set): Um conjunto de estados finais do autômato.
        """
        self.estados = set(estados)
        self.alfabeto = set(alfabeto)
        self.transicoes = collections.defaultdict(lambda: collections.defaultdict(set))
        
        # Copia as transições para garantir que os valores sejam conjuntos
        for estado_origem, simbolo_map in transicoes.items():
            for simbolo, destinos in simbolo_map.items():
                self.transicoes[estado_origem][simbolo].update(destinos)

        self.estado_inicial = estado_inicial
        self.estados_finais = set(estados_finais)

        # Validações básicas
        if self.estado_inicial not in self.estados:
            raise ValueError(f"O estado inicial '{self.estado_inicial}' não está no conjunto de estados.")
        if not self.estados_finais.issubset(self.estados):
            raise ValueError(f"Os estados finais '{self.estados_finais}' não são um subconjunto dos estados '{self.estados}'.")
        
        # Valida que todos os estados nas transições existem
        for origem, simbolo_map in self.transicoes.items():
            if origem not in self.estados:
                raise ValueError(f"Estado de origem '{origem}' na transição não está no conjunto de estados.")
            for simbolo, destinos in simbolo_map.items():
                if simbolo not in self.alfabeto:
                    raise ValueError(f"Símbolo '{simbolo}' na transição não está no alfabeto.")
                for destino in destinos:
                    if destino not in self.estados:
                        raise ValueError(f"Estado de destino '{destino}' na transição não está no conjunto de estados.")


    def __str__(self):
        """
        Retorna uma representação em string do autômato para fácil visualização.
        """
        s = "--- Autômato Finito ---\n"
        s += f"Estados: {sorted(list(self.estados))}\n"
        s += f"Alfabeto: {sorted(list(self.alfabeto))}\n"
        s += f"Estado Inicial: {self.estado_inicial}\n"
        s += f"Estados Finais: {sorted(list(self.estados_finais))}\n"
        s += "Transições:\n"
        # Ordena as chaves para saída consistente
        for estado_origem in sorted(list(self.transicoes.keys())):
            for simbolo in sorted(list(self.transicoes[estado_origem].keys())):
                destinos = sorted(list(self.transicoes[estado_origem][simbolo]))
                # Formata a transição para mostrar o conjunto de destinos
                s += f"  ({estado_origem}, {simbolo}) -> {destinos}\n"
        return s

# 2. Funções para ler e salvar autômatos em um arquivo

def ler_automato_de_arquivo(caminho_arquivo):
    """
    Lê a definição de um autômato de um arquivo de texto e retorna um objeto AFND.

    Formato do arquivo esperado:
    # Estados
    q0,q1,q2
    # Alfabeto
    a,b
    # Estado Inicial
    q0
    # Estados Finais
    q2
    # Transicoes
    q0,a,q0,q1
    q0,b,q0
    q1,a,q2
    q1,b,q2
    """
    estados = set()
    alfabeto = set()
    estado_inicial = None
    estados_finais = set()
    transicoes_raw = collections.defaultdict(lambda: collections.defaultdict(set))

    current_section = None
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:  # Ignora linhas vazias
                    continue
                if line.startswith('#'):
                    if line == '# Estados':
                        current_section = 'estados'
                    elif line == '# Alfabeto':
                        current_section = 'alfabeto'
                    elif line == '# Estado Inicial':
                        current_section = 'estado_inicial'
                    elif line == '# Estados Finais':
                        current_section = 'estados_finais'
                    elif line == '# Transicoes':
                        current_section = 'transicoes'
                    else:
                        current_section = None # Ignora outras linhas de comentário
                    continue

                if current_section == 'estados':
                    estados.update(line.split(','))
                elif current_section == 'alfabeto':
                    alfabeto.update(line.split(','))
                elif current_section == 'estado_inicial':
                    estado_inicial = line
                elif current_section == 'estados_finais':
                    estados_finais.update(line.split(','))
                elif current_section == 'transicoes':
                    parts = line.split(',')
                    if len(parts) < 3:
                        raise ValueError(f"Formato de transição inválido: '{line}'. Esperado 'origem,simbolo,destino1,destino2,...'")
                    
                    origin_state = parts[0]
                    symbol = parts[1]
                    destination_states = set(parts[2:])
                    
                    transicoes_raw[origin_state][symbol].update(destination_states)
    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho_arquivo}' não encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao ler o arquivo '{caminho_arquivo}': {e}")
        return None

    # Garante que todos os estados mencionados nas transições são incluídos no conjunto de estados
    for origin, symbol_map in transicoes_raw.items():
        estados.add(origin)
        for symbol, destinations in symbol_map.items():
            estados.update(destinations)

    return AFND(estados, alfabeto, transicoes_raw, estado_inicial, estados_finais)

def salvar_automato_em_arquivo(automato, caminho_arquivo):
    """
    Salva a definição de um objeto AFND em um arquivo de texto.

    Args:
        automato (AFND): O objeto AFND a ser salvo.
        caminho_arquivo (str): O caminho do arquivo onde o autômato será salvo.
    """
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            f.write("# Estados\n")
            f.write(",".join(sorted(list(automato.estados))) + "\n\n")

            f.write("# Alfabeto\n")
            f.write(",".join(sorted(list(automato.alfabeto))) + "\n\n")

            f.write("# Estado Inicial\n")
            f.write(automato.estado_inicial + "\n\n")

            f.write("# Estados Finais\n")
            f.write(",".join(sorted(list(automato.estados_finais))) + "\n\n")

            f.write("# Transicoes\n")
            # Ordena para garantir uma saída consistente no arquivo
            for estado_origem in sorted(list(automato.transicoes.keys())):
                for simbolo in sorted(list(automato.transicoes[estado_origem].keys())):
                    destinos = sorted(list(automato.transicoes[estado_origem][simbolo]))
                    f.write(f"{estado_origem},{simbolo},{','.join(destinos)}\n")
        print(f"Autômato salvo com sucesso em '{caminho_arquivo}'.")
    except Exception as e:
        print(f"Erro ao salvar o autômato em '{caminho_arquivo}': {e}")

# 3. Função para determinizar um AFND usando o método dos subconjuntos

def determinizar_afnd(afnd):
    """
    Converte um AFND para um AFD equivalente usando o método dos subconjuntos.
    Retorna a parte acessível do AFD resultante.

    Args:
        afnd (AFND): O autômato finito não-determinístico a ser determinizado.

    Returns:
        AFND: Um novo objeto AFND que representa o AFD equivalente.
              Os nomes dos estados do AFD serão representações de frozensets
              dos estados do AFND original (ex: "{q0,q1}").
    """
    # O estado inicial do AFD é o conjunto que contém o estado inicial do AFND
    novo_estado_inicial_set = frozenset({afnd.estado_inicial})
    
    # Fila para os estados do AFD a serem processados (cada elemento é um frozenset de estados do AFND)
    fila = collections.deque([novo_estado_inicial_set])
    
    # Conjunto de estados do AFD já processados
    estados_processados = {novo_estado_inicial_set}
    
    # Mapeamento de frozenset para o nome do estado no AFD resultante (para legibilidade)
    # Ex: frozenset({'q0', 'q1'}) -> 's_{q0,q1}' ou 'q0_q1'
    mapa_nomes_estados = {novo_estado_inicial_set: "{" + ",".join(sorted(list(novo_estado_inicial_set))) + "}"}

    novo_estados = set()
    novo_transicoes = collections.defaultdict(lambda: collections.defaultdict(set))
    novo_estados_finais = set()

    # Adiciona o nome do estado inicial do AFD ao conjunto de estados do AFD
    novo_estados.add(mapa_nomes_estados[novo_estado_inicial_set])

    # Verifica se o estado inicial do AFD é final
    if any(s in afnd.estados_finais for s in novo_estado_inicial_set):
        novo_estados_finais.add(mapa_nomes_estados[novo_estado_inicial_set])

    while fila:
        current_afd_state_set = fila.popleft() # Pega o próximo estado (subconjunto) a ser processado
        current_afd_state_name = mapa_nomes_estados[current_afd_state_set]

        for simbolo in afnd.alfabeto:
            next_afnd_state_set = set()
            # Calcula o próximo estado do AFND para cada estado no subconjunto atual
            for afnd_state_member in current_afd_state_set:
                if afnd_state_member in afnd.transicoes and simbolo in afnd.transicoes[afnd_state_member]:
                    next_afnd_state_set.update(afnd.transicoes[afnd_state_member][simbolo])
            
            # Converte o conjunto resultante para frozenset para que possa ser usado como chave
            next_afnd_state_frozenset = frozenset(next_afnd_state_set)

            # Se o conjunto resultante estiver vazio, não há transição para este símbolo a partir deste estado do AFD
            if not next_afnd_state_frozenset:
                continue

            # Se este novo estado do AFD (subconjunto) ainda não foi processado
            if next_afnd_state_frozenset not in estados_processados:
                fila.append(next_afnd_state_frozenset)
                estados_processados.add(next_afnd_state_frozenset)
                
                # Gera um nome legível para o novo estado do AFD
                new_afd_state_name = "{" + ",".join(sorted(list(next_afnd_state_frozenset))) + "}"
                mapa_nomes_estados[next_afnd_state_frozenset] = new_afd_state_name
                
                # Adiciona o novo estado do AFD ao conjunto de estados do AFD
                novo_estados.add(new_afd_state_name)

                # Verifica se o novo estado do AFD é final
                if any(s in afnd.estados_finais for s in next_afnd_state_frozenset):
                    novo_estados_finais.add(new_afd_state_name)
            
            # Adiciona a transição ao novo AFD
            next_afd_state_name = mapa_nomes_estados[next_afnd_state_frozenset]
            # Para um AFD, a transição é para um *único* estado (o subconjunto)
            novo_transicoes[current_afd_state_name][simbolo].add(next_afd_state_name)
    
    # O nome do estado inicial do AFD precisa ser o nome mapeado
    nome_estado_inicial_afd = mapa_nomes_estados[novo_estado_inicial_set]

    # Constrói e retorna o AFD resultante
    return AFND(novo_estados, afnd.alfabeto, novo_transicoes, nome_estado_inicial_afd, novo_estados_finais)

# --- Teste com Exemplos de Autômatos ---

# Exemplo 1: AFND simples
print("--- Exemplo 1: AFND Simples ---")
estados_simples = {'q0', 'q1', 'q2'}
alfabeto_simples = {'a', 'b'}
estado_inicial_simples = 'q0'
estados_finais_simples = {'q2'}
transicoes_simples = {
    'q0': {
        'a': {'q0', 'q1'},
        'b': {'q0'}
    },
    'q1': {
        'b': {'q2'}
    }
}
afnd_simples = AFND(estados_simples, alfabeto_simples, transicoes_simples, estado_inicial_simples, estados_finais_simples)
print("AFND Original:")
print(afnd_simples)

salvar_automato_em_arquivo(afnd_simples, "afnd_simples.txt")
afnd_lido_simples = ler_automato_de_arquivo("afnd_simples.txt")
print("\nAFND Lido do arquivo:")
print(afnd_lido_simples)

afd_simples_equivalente = determinizar_afnd(afnd_simples)
print("\nAFD Equivalente (Exemplo Simples):")
print(afd_simples_equivalente)
print(f"Número de estados no AFD simples: {len(afd_simples_equivalente.estados)}")
salvar_automato_em_arquivo(afd_simples_equivalente, "afd_simples_equivalente.txt")


# Exemplo 2: AFND que exige uma quantidade exponencial de estados (para n=3)
# Este AFND reconhece a linguagem (a+b)*a(a+b)^(n-1)
# Para n=3, reconhece strings que contêm 'a' na antepenúltima posição.
print("\n--- Exemplo 2: AFND com Explosão Exponencial (n=3) ---")
estados_exp = {'q0', 'q1', 'q2', 'q3'}
alfabeto_exp = {'a', 'b'}
estado_inicial_exp = 'q0'
estados_finais_exp = {'q3'}

transicoes_exp = {
    'q0': {
        'a': {'q0', 'q1'}, # Transição não-determinística
        'b': {'q0'}
    },
    'q1': {
        'a': {'q2'},
        'b': {'q2'}
    },
    'q2': {
        'a': {'q3'},
        'b': {'q3'}
    },
    'q3': {
        # Sem transições explícitas significa que vai para o conjunto vazio.
        # Para clareza, poderíamos ter: 'a': set(), 'b': set()
    }
}

afnd_exponencial = AFND(estados_exp, alfabeto_exp, transicoes_exp, estado_inicial_exp, estados_finais_exp)
print("AFND Original (Exemplo Exponencial):")
print(afnd_exponencial)

salvar_automato_em_arquivo(afnd_exponencial, "afnd_exponencial_n3.txt")
afnd_lido_exp = ler_automato_de_arquivo("afnd_exponencial_n3.txt")
print("\nAFND Lido do arquivo (Exponencial):")
print(afnd_lido_exp)

afd_equivalente_exp = determinizar_afnd(afnd_exponencial)
print("\nAFD Equivalente (Resultante da Determinizaçao Exponencial):")
print(afd_equivalente_exp)
print(f"Número de estados no AFD exponencial: {len(afd_equivalente_exp.estados)}")
salvar_automato_em_arquivo(afd_equivalente_exp, "afd_equivalente_exponencial_n3.txt")

# Você pode verificar os arquivos gerados:
# afnd_simples.txt
# afd_simples_equivalente.txt
# afnd_exponencial_n3.txt
# afd_equivalente_exponencial_n3.txt