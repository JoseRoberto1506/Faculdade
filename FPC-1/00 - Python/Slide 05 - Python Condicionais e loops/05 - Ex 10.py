while True:
    numero = int(input("Digite um número inteiro: "))
    if numero == 99:
        break
    if (numero % 2 != 0) and (numero > 0):
        print(f"{numero} é um número ímpar positivo")
