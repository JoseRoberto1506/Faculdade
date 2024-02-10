while True:
    numero = int(input("Você deseja ver a tabuada de que número? "))
    print("-" * 15)
    for i in range(1, 11):
        print(f"{numero} x {i:2} = {numero * i:2}")
    print("-" * 15)

    continuar = str(input("Você deseja ver a tabuada de outro número? (S/N): ")).strip().upper()
    if continuar == 'N':
        break
