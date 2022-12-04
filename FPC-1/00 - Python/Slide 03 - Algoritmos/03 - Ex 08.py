numero_1 = int(input("Primeiro número do intervalo: "))
numero_2 = int(input("Segundo número do intervalo: "))

for i in range(numero_1, numero_2 + 1):
    primo = True
    for j in range(2, i):
        if i % j == 0:
            primo = False
            break
    if primo == True:
        print(i)
