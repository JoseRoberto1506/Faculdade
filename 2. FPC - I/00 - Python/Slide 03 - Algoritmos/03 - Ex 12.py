j, k, soma = 37, 38, 0
for i in range(1, 38):
    soma += j * (k / i)
    j -= 1
    k -= 1
print(soma)
