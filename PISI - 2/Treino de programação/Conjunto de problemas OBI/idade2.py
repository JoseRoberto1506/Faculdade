# Loop para pedir a idade de dona Mônica até que a restrição da idade seja obedecida
while True:
    idade_monica = int(input())
    if 40 <= idade_monica <= 110:
        break

def idade_filhos():
    '''Função para pegar a idade de dois filhos'''
    a = int(input())
    b = int(input())
    return a, b

# Loop para pedir a idade dos dois filhos até que elas obedeçam as restrições
while True:
    idade_filho1, idade_filho2 = idade_filhos()

    if ((1 <= idade_filho1 < idade_monica) and 
        (1 <= idade_filho2 < idade_monica) and 
        (idade_filho1 != idade_filho2)):
        break

# Calculando idade do filho 3 e colocando as idades em uma lista
idade_filho3 = idade_monica - (idade_filho1 + idade_filho2)
idade_filhos = [idade_filho1, idade_filho2, idade_filho3]

# Imprimindo idade do filho mais velho
print(max(idade_filhos))
