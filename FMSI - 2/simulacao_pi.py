# Simulação do problema 2: Cálculo do número pi
# Alunos: José Roberto e Thales Mayrinck

def main():
    xminimo, xmaximo, yminimo, ymaximo, tot_pontos = -1, 1, -1, 1, 100000
    print([calcular_pi(xminimo, xmaximo, yminimo, ymaximo, tot_pontos) for _ in range(10)])


def calcular_pi(xmin, xmax, ymin, ymax, n_pontos):
    from random import uniform

    # Quantidade de pontos que estão dentro do círculo
    contador = 0
    # Gerar n pontos
    for _ in range(n_pontos):
        x = uniform(xmin, xmax)
        y = uniform(ymin, ymax)
        # Para o ponto estar dentro do cícrulo é preciso que: x^2 + y^2 <= r^2
        # Nesse problema o raio é igual a 1
        if (x**2) + (y**2) <= 1:
            contador += 1

    # Cálculo da probabilidade
    # Nesse problema: pi = 4 * (pontos dentro do cícrulo / total de pontos)
    return round(4 * contador / n_pontos, 2)


main()