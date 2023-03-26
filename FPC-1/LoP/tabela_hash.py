def main():
    entrada = [int(i) for i in input().split()]
    n_containers, tam_container, n_insercoes = entrada[0], entrada[1], entrada[2]
    nums_insercao = [entrada[i] for i in range(3, n_insercoes + 3)]
    nums_busca = entrada[n_insercoes + 3 : ]
    tabela = insercao(nums_insercao, n_containers, tam_container)
    consultar(tabela, nums_busca, n_containers, tam_container)


def hash(k, n_cont):
    # Função hash para determinar qual será o container
    return k % n_cont
    
    
def insercao(nums_to_insert, qntde_containers, tam_cont):
    # Função para inserir os números na tabela hash
    table = [None] * (qntde_containers * tam_cont)
    for num in nums_to_insert:
        container = hash(num, qntde_containers)
        index_container = container * tam_cont
        for i in range(index_container, index_container + 3):
            if table[i] == None:
                table[i] = num
                break
    
    return table


def consultar(table, nums_to_search, qtde_containers, tam_cont):
    # Função para consultar os números na tabela hash
    for num in nums_to_search:
        c = 0
        container = hash(num, qtde_containers)
        index_container = container * tam_cont
        for i in range(index_container, index_container + 3):
            c += 1
            if table[index_container] == None or table[i] == num:
                break
        print(c, end=' ')


main()
