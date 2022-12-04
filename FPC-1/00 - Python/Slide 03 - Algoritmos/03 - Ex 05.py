while True:
    a = int(input("A: "))
    b = int(input("B: "))
    if a < b:
        break

soma = 0
for i in range(a, b+1):
    if i % 2 == 0:
        soma += i**3

print(soma)
