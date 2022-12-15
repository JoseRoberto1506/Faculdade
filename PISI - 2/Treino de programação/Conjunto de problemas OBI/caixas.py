def pegar_tamanho_caixas():
    x = int(input())
    y = int(input())
    z = int(input())
    return x, y, z

while True:
    a, b, c = pegar_tamanho_caixas()

    if 1 <= a <= b <= c <= 1000:
        if a < b < c:
            print(1)
        elif a + b < c:
            print(1)
        elif a < b and b == c:
            print(2)
        elif a == b and b < c:
            print(2)
        elif a == b == c:
            print(3)
        break
