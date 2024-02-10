# Converter um número decimal para binário de forma recursiva
def conversão(n):
    global num_binario
    if n > 0:
        if n % 2 == 0:
            num_binario.append(0)
            num = int(n - (n / 2))
        else:
            num_binario.append(1)
            num = int(n - (n / 2) - 0.5)
        return conversão(num)
    else:
        num_binario.reverse()
        return num_binario

numero, num_binario = 10, []
conversão(numero)
for n in num_binario:
    print(n, end='')
