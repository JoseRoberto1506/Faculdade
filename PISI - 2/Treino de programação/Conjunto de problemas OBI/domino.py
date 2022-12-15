while True:
    n = int(input())
    if 0 <= n <= 10000:
        break

numero_peças = int(((n + 1) * (n + 2)) / 2)
print(numero_peças)
