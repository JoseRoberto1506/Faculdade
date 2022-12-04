nome = str(input("Digite seu nome: ")).strip().upper()
for i in range(len(nome)):
    print(nome[:i+1])
