preços = []
for i in range(3):
    preços.append(float(input("Digite o preço do produto: R$ ")))
preços.sort()
print(f"Você deve comprar o produto de preço R$ {preços[0]:.2f}")
