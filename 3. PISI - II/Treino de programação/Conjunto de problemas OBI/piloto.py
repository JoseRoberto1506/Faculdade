def pegar_distancias():
    '''Função para pegar as posições atuais das traseiras dos carros'''
    x = int(input())
    y = int(input())
    z = int(input())
    return x, y, z

while True:
    a, b, c = pegar_distancias()
    
    if (0 <= a <= 500) and (a < b < c) and (b < c <= 500):
        # O carro B precisa acelerar
        if (b - a) < (c - b):
            print(1)
        # O carro B precisa desacelerar
        elif (b - a) > (c - b):
            print(-1)
        # O carro B precisa manter a velocidade atual
        elif (b - a) == (c - b):
            print(0)
        break
