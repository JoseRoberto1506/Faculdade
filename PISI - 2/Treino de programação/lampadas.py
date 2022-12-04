# Quantidade de vezes que o interruptor será pressionado
quant = int(input())
# Lista com as operações feitas em cada interruptor
apertos = [int(i) for i in input().split()]

# Se a quantidade de apertos for par, a lâmapada estará apagada. Se a quantidade for ímpar, a lâmapada estará acesa.
# Verificando lâmpada 1
if apertos.count(1) % 2 == 0:
    print(0)
else:
    print(1)
# Verificando lâmpada 2
if apertos.count(2) % 2 == 0:
    print(0)
else:
    print(1)

# O programa está aceitando caso digite mais operações do que a informada em 'quant'