class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, percentual):
        return self.salario + (self.salario * (percentual / 100))
    
# Teste
nome_func = str(input("Nome: ")).strip().capitalize()
salario_func = float(input("Salário: R$ "))
funcionario = Funcionario(nome_func, salario_func)
print(f"R$ {funcionario.aumentar_salario(10):.2f}")
