class Aluno:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Equipe:
    def __init__(self, lista_de_alunos):
        self.lista_alunos = lista_de_alunos
        self.projeto = str()

class GerenciadorEquipes:
    def __init__(self):
        self.equipes = []

    