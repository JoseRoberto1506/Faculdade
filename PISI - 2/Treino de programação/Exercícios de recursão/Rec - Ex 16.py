# Unir dois arrays de forma recursiva
def unir(lista_a, lista_b, lista_n):
    if (len(lista_a) == 0) and (len(lista_b)) == 0:
        return lista_n
    else:
        if len(lista_a) > 0:
            lista_n.append(lista_a[0])
        if len(lista_b) > 0:
            lista_n.append(lista_b[0])
        return unir(lista_a[1:], lista_b[1:], lista_n)

lista_1 = [1, 3, 5, 7, 9]
lista_2 = [2, 4, 6, 8, 10]
lista_nova = []
print(unir(lista_1, lista_2, lista_nova))
