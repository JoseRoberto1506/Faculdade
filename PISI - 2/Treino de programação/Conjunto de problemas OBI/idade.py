idades = []
for i in range(0, 3):
    while True:
        n = int(input())
        if 5 <= n <= 100:
            idades.append(n)
            break

idades.sort()
print(idades[1])
