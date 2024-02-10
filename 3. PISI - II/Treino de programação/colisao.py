x0a, y0a, x1a, y1a = [int(i) for i in input().split()]
x0b, y0b, x1b, y1b = [int(i) for i in input().split()]

# Verificando se não há colisão em X
if x0b > x1a or x0a > x1b:
    print(0)
# Verificando se não há colisão em Y
elif y0b > y1a or y0a > y1b:
    print(0)
else:
    print(1)
