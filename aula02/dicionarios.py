# dicionarios armazenam elemetos em pares chave-valor
# sao criados usando chaves {}
# dicionarios sao mutaveis, ou seja, podem ser alterados depois de criados
# dicionarios sao indexados por chaves, ou seja, podemos acessar seus elementos usando as chaves
# sintaxe: dicionario = {chave1: valor1, chave2: valor2, ...}

elemento = {
    'nome': 'Hidrogenio',
    'simbolo': 'H',
    'numero_atomico': 1,
    'massa_atomica': 1.008,
}

print(f'Elemento: {elemento["nome"]}')
print(f'Simbolo: {elemento["simbolo"]}')
print(f'Numero Atomico: {elemento["numero_atomico"]}')
print(f'Massa Atomica: {elemento["massa_atomica"]}')
print(f'o dicionario tem {len(elemento)} elementos') # isso vai imprimir 4, pois o dicionario elemento tem 4 pares chave-valor  

# atualizar um valor no dicionario
elemento['massa_atomica'] = 1.00784
print(elemento) # isso vai imprimir o dicionario atualizado, com a massa atomica do hidrogenio corrigida para 1.00784   

elemento['perioodo'] = 1
print(elemento) # isso vai imprimir o dicionario atualizado, com a nova chave "periodo" e seu valor associado 1, pois dicionarios sao mutaveis e podemos adicionar novos pares chave-valor a qualquer momento   

del elemento['perioodo']
print(elemento) # isso vai imprimir o dicionario atualizado, sem a chave "periodo" e seu valor associado, pois o comando del remove a chave "periodo" e seu valor do dicionario elemento    

elemento.clear()
print(elemento) # isso vai imprimir {}, pois o metodo clear() remove todos os pares chave-valor do dicionario elemento, deixando-o vazio    

del elemento
print(elemento) # vai apagar completamente o dicionario elemento da memoria, e tentar imprimir elemento agora vai gerar um erro, pois o dicionario elemento nao existe mais. O comando del remove a variavel elemento da memoria, e nao apenas seu conteudo. Depois de usar del, a variavel elemento nao esta mais definida e nao pode ser usada.   


print(elemento.items()) # isso vai imprimir os pares chave-valor do dicionario elemento como uma lista de tuplas, onde cada tupla representa um par chave-valor. O metodo items() retorna uma vista dos itens do dicionario, que pode ser convertida em uma lista usando a funcao list(). Cada item da lista é uma tupla contendo a chave e o valor correspondente do dicionario.
for i in elemento.items():
    print(i) # isso vai imprimir cada par chave-valor do dicionario elemento em uma linha diferente, pois o metodo items() retorna uma vista dos itens do dicionario, que pode ser iterada usando um loop for. Cada item da vista é uma tupla contendo a chave e o valor correspondente do dicionario. O loop for percorre cada item da vista e imprime a tupla correspondente. 

print(elemento.keys()) # isso vai imprimir as chaves do dicionario elemento como uma lista, pois o metodo keys() retorna uma vista das chaves do dicionario, que pode ser convertida em uma lista usando a funcao list(). Cada item da lista é uma chave do dicionario. O metodo keys() retorna apenas as chaves do dicionario, sem os valores correspondentes.
for i in elemento.keys():
    print(i) # isso vai imprimir cada chave do dicionario elemento em uma linha diferente, pois o metodo keys() retorna uma vista das chaves do dicionario, que pode ser iterada usando um loop for. Cada item da vista é uma chave do dicionario. O loop for percorre cada item da vista e imprime a chave correspondente. 


print(elemento.values()) # isso vai imprimir os valores do dicionario elemento como uma lista, pois o metodo values() retorna uma vista dos valores do dicionario, que pode ser convertida em uma lista usando a funcao list(). Cada item da lista é um valor do dicionario. O metodo values() retorna apenas os valores do dicionario, sem as chaves correspondentes.  
for i in elemento.values():
    print(i) # isso vai imprimir cada valor do dicionario elemento em uma linha diferente, pois o metodo values() retorna uma vista dos valores do dicionario, que pode ser iterada usando um loop for. Cada item da vista é um valor do dicionario. O loop for percorre cada item da vista e imprime o valor correspondente.       

for i , j in elemento.items():
    print(f'{i}: {j}') # isso vai imprimir cada par chave-valor do dicionario elemento em uma linha diferente, no formato "chave: valor", pois o metodo items() retorna uma vista dos itens do dicionario, que pode ser iterada usando um loop for. Cada item da vista é uma tupla contendo a chave e o valor correspondente do dicionario. O loop for percorre cada item da vista e imprime a chave e o valor correspondentes usando a sintaxe de f-string para formatar a string de saída. O resultado é uma linha para cada par chave-valor do dicionario, no formato "chave: valor".    


