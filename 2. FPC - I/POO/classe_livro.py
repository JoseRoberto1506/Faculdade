class Livro:
    def __init__(self, nome, qtde_paginas, autor, preco):
        self.nome = nome
        self.qtde_paginas = qtde_paginas
        self.autor = autor
        self.preco = preco

    def get_preco(self):
        return self.preco
    
    def set_preco(self, novo_preco):
        self.preco = novo_preco

# Teste
nome_livro = str(input("Nome do livro: ")).strip()
tot_paginas = int(input("Quantidade de páginas: "))
autor_livro = str(input("Autor do livro: ")).strip().capitalize()
preco_livro = float(input("Preço: R$ "))
livro = Livro(nome_livro, tot_paginas, autor_livro, preco_livro)
print(f"R$ {livro.get_preco():.2f}")
novo_valor = float(input("Novo preço do livro: R$ "))
livro.set_preco(novo_valor)
print(f"R$ {livro.get_preco():.2f}")
