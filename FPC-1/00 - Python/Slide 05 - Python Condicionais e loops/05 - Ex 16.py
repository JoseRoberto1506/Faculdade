comissões = []

for _ in range(10):
    itens_vendidos = int(input("Quantidade de itens vendidos: "))
    if itens_vendidos <= 19:
        comissões.append(10)
    elif 20 <= itens_vendidos <= 49:
        comissões.append(15)
    elif 50 <= itens_vendidos <= 74:
        comissões.append(20)
    else:
        comissões.append(25)

print("Percentual de comissão de cada representante:")
for comissão in comissões:
    print(f"{comissão}%")
