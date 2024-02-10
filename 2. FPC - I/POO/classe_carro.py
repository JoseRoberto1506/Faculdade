class Carro:
    def __init__(self, km_por_litro):
        self.km_por_litro = km_por_litro
        self.tanque = 0
    
    def adicionar_gasolina(self, qtde_gasolina):
        self.tanque += qtde_gasolina

    def obter_gasolina(self):
        return self.tanque
    
    def andar(self, distancia):
        while distancia > 0:
            if self.tanque <= 0:
                break

            if distancia - self.km_por_litro >= 0:
                distancia -= self.km_por_litro
                self.tanque -= 1
            else:
                self.tanque -= 0.066 * distancia # 1 km = 0.66 litros
                distancia = 0

# Teste
meu_fusca = Carro(15)
meu_fusca.adicionar_gasolina(20)
meu_fusca.andar(100)
print(f"Combustível restante: {meu_fusca.obter_gasolina():.2f} litros")
