from datetime import date

class Livro:
    dataAluguel, dataDevolucao = None, None
    __qtdeAlugueis = 0

    def __init__(self, codigo, nome, autor):
        self.codigo = codigo
        self.nome = nome
        self.autor = autor
        
    def incrementaAluguel(self):
        self.__qtdeAlugueis += 1

    def getQtdeAlugueis(self):
        return self.__qtdeAlugueis


class Biblioteca:
    alugados, disponiveis = [], []

    def inserir(self, livro):
        self.disponiveis.append(livro)

    def alugar(self, objLivro, dataDevolucao): #dataDevolucao eh uma string no formato dd/mm/aaaa
        ok, mensagem = True, None

        if objLivro in self.disponiveis:
            for i in self.disponiveis:
                if i == objLivro:
                    i.incrementaAluguel()
                    i.dataAluguel = date.today()
                    i.dataDevolucao = dataDevolucao
                    self.alugados.append(i)
                    self.disponiveis.remove(i)
                    break
        elif objLivro in self.alugados:
            ok = False
            mensagem = "O livro ja esta alugado, infelizmente voce nao podera alugar"
        else:
            ok = False
            mensagem = "O livro nao existe"
        return (ok, mensagem)

    def devolver(self, codLivro):
        ok, mensagem = True, None
        for livro in self.alugados:
            if livro.codigo == codLivro:
                self.disponiveis.append(livro)
                self.alugados.remove(livro)
                break
        else:
            ok = False
            mensagem = "O livro nao esta alugado"
        return (ok, mensagem)

    def livroMaisAlugado(self):
        ok, mensagem, maior, nome = True, None, 0, None

        for livro in self.disponiveis:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                nome = livro.nome
        for livro in self.alugados:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                nome = livro.nome
        if maior == 0:
            ok = False
            mensagem = "Nenhum livro foi alugado ainda"
        else:
            mensagem = "O livro mais alugado e: %s (%d alugueis)"%(nome, maior)
        return (ok, mensagem)
    
    def livrosOrdenadosPorDataDeDevolucao(self):
        # Verificar qual é a maior data
        def comparar_datas(data_A, data_B):
            dia_a, mes_a, ano_a = data_A.split("/")
            dia_b, mes_b, ano_b = data_B.split("/")

            if int(ano_a) < int(ano_b): # Comparar ano
                return True
            elif int(ano_a) == int(ano_b):
                if int(mes_a) < int(mes_b): # Comparar mês
                    return True
                elif int(mes_a) == int(mes_b):
                    if int(dia_a) < int(dia_b): # Comparar dia
                        return True
            return False
        
        # Ordenação por ShellSort
        n = int(len(self.alugados))
        h = int(n / 2)
        while h > 0:
            for i in range(h, n):
                chave = self.alugados[i]
                j = i
                while j >= h and comparar_datas(chave.dataDevolucao, self.alugados[j - h].dataDevolucao):
                    self.alugados[j] = self.alugados[j - h]
                    j -= h
                self.alugados[j] = chave
            h = int(h / 2.2)
        return self.alugados


# Ler entrada e criar instância da classe Biblioteca
entrada = [i for i in input().split(",")]
qtde_livros = int(entrada.pop(0))
biblioteca = Biblioteca()

# Criar objeto livro e adicioná-lo na biblioteca
for _ in range(qtde_livros):
    livro = Livro(entrada.pop(0), entrada.pop(0), entrada.pop(0))
    biblioteca.inserir(livro)

# Alugar livros
n = int(len(entrada))
for i in range(0, n, 2):
    for livro in biblioteca.disponiveis:
        if livro.codigo == entrada[i]:
            biblioteca.alugar(livro, entrada[i + 1])

# Ordenar e imprimir saída
livros_ordenados = biblioteca.livrosOrdenadosPorDataDeDevolucao()
for livro in livros_ordenados:
    print(livro.codigo, end=" ")
