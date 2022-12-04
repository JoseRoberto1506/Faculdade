string_1 = str(input("Digite algo: ")).strip()
string_2 = str(input("Digite algo mais uma vez: "))

print(f"String 1: {string_1}")
print(f"String 2: {string_2}")
print(f"Tamanho de '{string_1}': {len(string_1)}")
print(f"Tamanho de '{string_2}': {len(string_2)}")

if len(string_1) != len(string_2):
    print("As duas strings são de tamanhos diferentes")
else:
    print("As duas strings são do mesmo tamanho")
if string_1 != string_2:
    print("As duas strings possuem conteúdos diferentes")
else:
    print("As duas strings possuem conteúdos iguais")
