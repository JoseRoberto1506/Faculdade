Alice_par = Bob_par = False
soma = 0

# Loop para verificar quem jogou par e fazer a soma dos dedos
for i in range(0, 3):
    # O loop infinito será quebrado apenas quando for digitado um número que obedeça às restrições
    while True:
        n = int(input())
        if i == 0:
            if 0 <= n <= 1:
                # Verificar quem escolheu Par
                if n == 0:
                    Alice_par = True
                elif n == 1:
                    Bob_par = True
                break
        else:
            # Soma dos dedos
            if 0 <= n <= 5:
                soma += n
                break

# Resultado caso Alice tenha escolhido Par
if Alice_par == True:
    if soma % 2 == 0:
        print(0)
    else:
        print(1)
# Resultado caso Bob tenha escolhido Par
elif Bob_par == True:
    if soma % 2 == 0:
        print(1)
    else:
        print(0)
