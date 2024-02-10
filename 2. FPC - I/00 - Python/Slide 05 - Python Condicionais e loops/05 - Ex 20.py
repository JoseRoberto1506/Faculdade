maior = menor = soma_total = 0

for i in range(100):
    temperatura = float(input("Digite a temperatura (°C): "))
    if i == 0:
        maior = menor = temperatura
    else:
        if temperatura > maior:
            maior = temperatura
        elif temperatura < menor:
            menor = temperatura
    soma_total += temperatura

media = soma_total / 100
print(f"Maior temperatura: {maior}°C")
print(f"Menor temperatura: {menor}°C")
print(f"Média das temperaturas: {media:.2f}°C")
