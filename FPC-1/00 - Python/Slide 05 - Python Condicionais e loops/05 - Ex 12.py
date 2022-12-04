numeros_primos = [2]
i, total = 3, 1

while total < 15:
    primo = True
    for j in range(2, i):
        if i % j == 0:
            primo = False
            break
    if primo == True:
        numeros_primos.append(i)
        total += 1
    i += 1

print("Lista dos 15 primeiros números primos:")
print(numeros_primos)
