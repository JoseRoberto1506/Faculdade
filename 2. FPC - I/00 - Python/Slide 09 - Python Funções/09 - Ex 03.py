def sinal_numero(n):
    if n > 0:
        return "P"
    else:
        return "N"

numero = int(input("Digite um número inteiro: "))
print(sinal_numero(numero))
