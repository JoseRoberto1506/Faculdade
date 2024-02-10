distancia = int(input("Distância (Km): "))
tempo = int(input("Tempo (horas): "))
vel_media = distancia / tempo

if vel_media > 110:
    print("A velocidade média foi superior ao limite de 110 Km/h")
else:
    print("A velocidade média foi dentro do limite de 110 km/h")
