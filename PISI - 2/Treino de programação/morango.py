medidas = []
for i in range(0, 4):
    while True:
        n = int(input())
        if 1 <= n <= 100:
            medidas.append(n)
            break

area1 = medidas[0] * medidas[1]
area2 = medidas[2] * medidas[3]
if area1 > area2:
    print(area1)
elif area2 > area1:
    print(area2)
