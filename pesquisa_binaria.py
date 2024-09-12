# Código demonstrando um algorítimo muito conhecido, chamado de pesquisa binária, com tempo de execução O(logN)
def pesquisa_binaria (lista, numero):
    lista.sort()
    baixo = 0
    alto = len(lista) - 1
    
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        
        if chute == numero:
            print(f'O índice que foi encontrado o número é : {meio}')
            return
              
        elif chute > numero:
            alto = meio - 1
            
        elif chute < numero:
            baixo = meio + 1
        
    print('O número não foi encontrado')
        
pesquisa_binaria([0, 1, 2, 3, 4, 5, 6, 7], 5)
# Pode inserir qualquer lista aqui e o outro argumento seria o número que quer ser encontrado, acima está apenas um exemplo