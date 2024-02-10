while True:
    distancia = int(input())
    if 0 <= distancia <= 2000:
        break

if distancia <= 800:
    print(1)
elif 800 < distancia <= 1400:
    print(2)
else:
    print(3)
