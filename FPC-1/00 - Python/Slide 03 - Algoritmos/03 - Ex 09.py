soma, i, j = 0, 1000, 1
while j <= 50:
    if j % 2 == 0:
        soma -= i/j
    else:
        soma += i/j
    i -= 3
    j += 1

print(soma)
