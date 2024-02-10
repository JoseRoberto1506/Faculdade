class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def calcular_perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c
    
    def get_maior_lado(self):
        if (self.lado_a >= self.lado_b) and (self.lado_a >= self.lado_c):
            return self.lado_a
        elif (self.lado_b >= self.lado_a) and (self.lado_b >= self.lado_c):
            return self.lado_b
        else:
            return self.lado_c
        
# Teste
medidas = [int(i) for i in input("Medidas do triângulo: ").split()]
triangulo = Triangulo(medidas[0], medidas[1], medidas[2])
print(triangulo.calcular_perimetro())
print(triangulo.get_maior_lado())
