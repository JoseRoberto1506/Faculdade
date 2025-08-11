from automato import Automato, determinizar

# Exemplo de AFND com crescimento exponencial
# Linguagem: palavras com '1' na quarta posição após uma sequência arbitrária de '0' e '1'
afnd_exponencial = Automato(
    tipo="AFND",
    alfabeto=["0", "1"],
    estados=["q0", "q1", "q2", "q3", "q4"],
    inicial="q0",
    finais=["q4"],
    transicoes={
        "q0": {
            "0": ["q0"],
            "1": ["q0", "q1"]
        },
        "q1": {
            "0": ["q2"],
            "1": ["q2"]
        },
        "q2": {
            "0": ["q3"],
            "1": ["q3"]
        },
        "q3": {
            "1": ["q4"]
        }
    }
)

# Salva o AFND original
afnd_exponencial.salvar("afnd_exemplo.json")
print("AFND salvo em afnd_exemplo.json")

# Determiniza e salva o AFD resultante
afd_resultante = determinizar(afnd_exponencial)
afd_resultante.salvar("afd_resultante.json")
print("AFD resultante salvo em afd_resultante.json")

# Mostra o número de estados no AFD
total_estados = len(afd_resultante.estados)
print(f"AFD gerado possui {total_estados} estados.")
