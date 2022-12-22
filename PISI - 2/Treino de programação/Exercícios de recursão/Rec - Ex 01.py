# Análise combinatória calculada de forma recursiva
def comb(n, k):
    if k == 1:
        return n
    elif k == n:
        return 1
    elif (1 < k < n):
        return comb(n-1, k-1) + comb(n-1, k)

# Análise combinatória calculada de forma não recursiva
def comb_2(n, k):
    from math import factorial as fat
    result = int(fat(n) / (fat(k) * fat(n-k)))
    return result

print(comb(5, 3))
print(comb_2(5, 3))
