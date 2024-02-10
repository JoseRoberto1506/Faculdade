numero = int(input("Quantidade de tabuadas: "))
i = 1
while i <= numero:
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print()
    i += 1
