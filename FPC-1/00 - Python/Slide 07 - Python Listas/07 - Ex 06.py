from random import randint
temperaturas = [randint(0, 31) for i in range(12)]
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
media_anual = sum(temperaturas) / 12

print("Temperaturas mensais no ano:")
print(f"{temperaturas}\n")
print(f"Média anual das temperaturas: {media_anual:.2f}°C\n")
print("Temperaturas acima da média anual:")
for pos, temp in enumerate(temperaturas):
    if temp > media_anual:
        print(f"{meses[pos]}: {temp}°C")
