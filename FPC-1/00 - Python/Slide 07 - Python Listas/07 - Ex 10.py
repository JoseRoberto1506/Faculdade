respostas = []

resp_1 = str(input("Telefonou para a vítima? (S/N) ")).strip().upper()
if resp_1 == "S":
    respostas.append(resp_1)

resp_2 = str(input("Esteve no local do crime? (S/N) ")).strip().upper()
if resp_2 == "S":
    respostas.append(resp_2)

resp_3 = str(input("Mora perto da vítima? (S/N) ")).strip().upper()
if resp_3 == "S":
    respostas.append(resp_3)

resp_4 = str(input("Tinha dívidas com a vítima? (S/N) ")).strip().upper()
if resp_4 == "S":
    respostas.append(resp_4)

resp_5 = str(input("Já trabalhou com a vítima? (S/N) ")).strip().upper()
if resp_5 == "S":
    respostas.append(resp_5)

resps_positivas = respostas.count("S")
if resps_positivas < 2:
    print("Inocente")
elif resps_positivas == 2:
    print("Suspeita")
elif resps_positivas < 5:
    print("Cúmplice")
else:
    print("Assassino")
