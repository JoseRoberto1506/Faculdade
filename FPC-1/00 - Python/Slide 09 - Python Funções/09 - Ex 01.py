def soma_imposto(taxa, custo):
    novo_valor = custo + (custo * (taxa / 100))
    return novo_valor

preço = float(input("Preço do item: R$  "))
taxa_imposto = float(input("Taxa do imposto (%): "))
preço_com_imposto = soma_imposto(taxa_imposto, preço)

print(f"Após a incidência de {taxa_imposto:.2f}% de imposto, o produto custará R$ {preço_com_imposto:.2f}")
