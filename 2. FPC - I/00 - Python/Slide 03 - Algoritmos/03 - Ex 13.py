lado_1 = int(input("Digite o lado 1: "))
lado_2 = int(input("Digite o lado 2: "))
lado_3 = int(input("Digite o lado 3: "))

if (lado_1 < lado_2 + lado_3) and (lado_2 < lado_1 + lado_3) and (lado_3 < lado_1 + lado_2):
    if lado_1 == lado_2 == lado_3:
        print("Equilátero")
    elif (lado_1 != lado_2) and (lado_1 != lado_3) and (lado_2 != lado_3):
        print("Escaleno")
    else:
        print("Isósceles")
else:
    print("Os lados fornecidos não formam um triângulo")
