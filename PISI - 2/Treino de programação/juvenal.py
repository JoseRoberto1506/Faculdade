def f(n, stepcount):
    stepcount += 1
    if n > 1:
        if n % 2 == 0:
            return f(n/2, stepcount)
        else:
            return f(3*n+1, stepcount)
    return stepcount

def g(a, b):
    '''
    Função para calcular quantas chamadas recursivas são necessárias para que F(n) atinja o caso base
    '''
    maior_quant_passos = 0
    # Verificando o maior valor quando 'n' está no intervalo [A, B]
    while a <= b:
        steps = f(a, 0)
        if steps > maior_quant_passos:
            maior_quant_passos = steps
        a += 1
    return maior_quant_passos

def maiores_valores(testes):
    '''
    Função para retornar o maior valor de 'n' em cada caso de teste
    '''
    maiores_valores = []
    # Inteiros A e B
    for _ in range(t):
        while True:
            a, b = [int(i) for i in input().split()]
            if 1 <= a <= b <= 100000:
                maior_valor = g(a, b)
                # Colocando o maior valor de cada teste em uma lista com os maiores valores
                maiores_valores.append(maior_valor)
                break
    
    for i, v in enumerate(maiores_valores):
        print(f"Caso {i+1}: {v}")

# Número de casos de teste
while True:
    t = int(input("Número de casos de teste: "))
    if 1 <= t <= 100:
        maiores_valores(t)
        break
