# Input para a quota mensal em megabytes
while True:
    megabytes = int(input())
    if 1 <= megabytes <= 100:
        break
# Input para o número de meses
while True:
    meses = int(input())
    if 1 <= meses <= 100:
        break

# Variável para armazenar a quantidade de megabytes disponíveis para o mês N+1
proximo_mes = megabytes

for i in range(0, meses):
    while True:
        n = int(input())
        # Verificando se o consumo do mês está dentro do limite e atualizando a variável do limite
        if n <= proximo_mes:
            proximo_mes = proximo_mes - n + megabytes
            break

print(proximo_mes)
