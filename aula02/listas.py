#listas [] em python e uma estrutura de dados que armazena uma coleção ordenada de itens, que podem ser de tipos diferentes, como números, strings ou até outras listas.
           
#sintaxe nome_lista = [item1, item2, item3, ...]

notas = [8.5, 7.0, 9.5, 6.0, 10.0] #lista de notas
print(notas)

# cada elemento da lista tem um indice, que começa em 0 
# cada elemento pode ser acessado usando colchetes e o indice do elemento desejado
print(notas[0]) #acessa o primeiro elemento da lista
print(notas[2]) #acessa o terceiro elemento da lista
print(notas[4]) #acessa o quinto elemento da lista

# as listas podem ser concatenadas usando o operador +
n1 = [8.5, 7.0, 9.5]
n2 = [8.5, 7.0]
todas_notas = n1 + n2
print(todas_notas)
print(todas_notas[3]) #acessa o quarto elemento da lista todas_notas
print(todas_notas[-1])#acessa o ultimo elemento da lista todas_notas
print(todas_notas[-2])#acessa o penultimo elemento da lista todas_notas

n1 = [8.5, 7.0, 9.5]
n2 = [8.5, 7.0]
todas_notas = n1 + n2
todas_notas[0] = 6.0 #modifica o primeiro elemento da lista todas_notas
print(todas_notas)

n1 = [8.5, 7.0, 9.5]
n2 = [8.5, 7.0]
todas_notas = n1 + n2
print(todas_notas[:3]) #acessa os tres primeiros elementos da lista todas_notas que sao os elementos de indice 0, 1 e 2
print(todas_notas[2:5]) #acessa do terceiro ao quinto elemento da lista todas_notas
print(todas_notas[::2]) #acessa todos os elementos da lista todas_notas pulando de 2 em 2
print(todas_notas[::-1]) #acessa todos os elementos da lista todas_notas em ordem inversa
print(todas_notas[1::2]) #acessa todos os elementos da lista todas_notas a partir do segundo elemento pulando de 2 em 2 
print(todas_notas[:-2]) #acessa todos os elementos da lista todas_notas exceto os dois ultimos
print(todas_notas[:]) #acessa todos os elementos da lista todas_notas



n1 = [8.5, 7.0, 9.5]
n2 = [8.5, 7.0]
todas_notas = n1 + n2
print(len(todas_notas)) #retorna o tamanho da lista todas_notas len em ingles significa length (comprimento/tamanho)
print(sorted(todas_notas, reverse=True)) #retorna uma nova lista com os elementos de todas_notas ordenados em ordem de crescente sorted em ingles significa ordenar\ reverse=True para ordem decrescente isso signicifica que o maior valor vem primeiro
print(min(todas_notas)) #retorna o menor elemento da lista todas_notas min em ingles significa minimum (mínimo)
print(max(todas_notas)) #retorna o maior elemento da lista todas_notas max em ingles significa maximum (máximo)
print(sum(todas_notas)) #retorna a soma dos elementos da lista todas_notas sum em ingles significa soma 

valores = [10, 20, 30, 40, 50]
valores.append(60) #adiciona o elemento 60 ao final da lista valores append em ingles significa anexar\ adicionar
print(valores)  

valores = [10, 20, 30, 40, 50]
valores.insert(2, 25) #adiciona o elemento 25 na posição de indice 2 da lista valores insert em ingles significa inserir
print(valores)          

valores = [10, 20, 30, 40, 50]
valores.remove(30) #remove o elemento 30 da lista valores remove em ingles significa remover
print(valores)

valores = [10, 20, 30, 40, 50]
retirado = valores.pop() #remove e retorna o ultimo elemento da lista valores pop em ingles significa estourar\ retirar
print(valores)  
print(retirado)

valores = [10, 20, 30, 40, 50]
retirado = valores.pop(1) #remove e retorna o elemento de indice 1 da lista valores
print(valores)  
print(retirado) 

valores = [10, 20, 30, 40, 50]
valores.clear() #remove todos os elementos da lista valores clear em ingles significa limpar        
print(valores)

valores = [10, 20, 30, 40, 50]
indice = valores.index(30) #retorna o indice do elemento 30 na lista valores
print(indice)

valores = [10, 20, 30, 40, 50, 30]
count = valores.count(30) #retorna o número de ocorrências do elemento 30 na lista valores
print(count)

valores = [50, 20, 40, 10, 30]
valores.sort() #ordena os elementos da lista valores em ordem crescente sort em ingles significa ordenar
print(valores)

valores = [50, 20, 40, 10, 30]
valores.sort(reverse=True) #ordena os elementos da lista valores em ordem decrescente   
print(valores)

valores = [50, 20, 40, 10, 30]
valores.reverse() #inverte a ordem dos elementos da lista valores reverse em ingles significa inverter      
print(valores)

#listas podem conter elementos de tipos diferentes
mix = [10, "olá", 3.14, True, [1, 2, 3]]
print(mix)  
print(mix[1]) #acessa o segundo elemento da lista mix
print(mix[4]) #acessa o quinto elemento da lista mix que é outra lista
print(mix[4][2]) #acessa o terceiro elemento da lista que está dentro da lista mix
#listas podem ser aninhadas (listas dentro de listas)
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz)   
print(matriz[0]) #acessa a primeira linha da matriz
print(matriz[1][2]) #acessa o elemento da segunda linha e terceira coluna
#percorrendo uma lista com um loop for
notas = [8.5, 7.0, 9.5, 6.0, 10.0]
for nota in notas:
    print(nota)
#usando a função range para percorrer os indices da lista
notas = [8.5, 7.0, 9.5, 6.0, 10.0]
for i in range(len(notas)):
    print(f'nota na posição {i} é {notas[i]}')  
#verificando se um elemento está na lista usando o operador in
notas = [8.5, 7.0, 9.5, 6.0, 10.0]
print(9.5 in notas) #retorna True se 9.5 estiver na lista notas
print(5.0 in notas) #retorna False se 5.0 não estiver na lista notas    
#verificando se um elemento não está na lista usando o operador not in
notas = [8.5, 7.0, 9.5, 6.0, 10.0]
print(9.5 not in notas) #retorna False se 9.5 estiver na lista notas
print(5.0 not in notas) #retorna True se 5.0 não    estiver na lista notas  
#copiando uma lista
notas = [8.5, 7.0, 9.5, 6.0, 10.0]
copia_notas = notas.copy() #cria uma cópia da lista notas   
print(copia_notas)
#outra forma de copiar uma lista
notas = [8.5, 7.0, 9.5, 6.0, 10.0]
copia_notas = list(notas) #cria uma cópia da lista notas usando a função list
print(copia_notas)  
#listas podem ser usadas para armazenar coleções de dados relacionados
alunos = ["Alice", "Bob", "Charlie", "David"]
notas = [8.5, 7.0, 9.5, 6.0]
for i in range(len(alunos)):
    print(f'Aluno: {alunos[i]}, Nota: {notas[i]}')  
#listas podem ser usadas como pilhas (LIFO - Last In First Out)
pilha = []
pilha.append(1) 
pilha.append(2)
pilha.append(3)
print(pilha)  
ultimo = pilha.pop() #remove o ultimo elemento adicionado à pilha   
print(ultimo)
print(pilha)    


nome = input('digite seu nome')
print(f'o nome digitado foi {nome}')
idade = int (input('digite sua idade: '))
print(f'sua idade e {idade}')

if idade <= 17:
    print('voce e menor de idade nao pode consumir bebidas alcoolicas')
else:
    print('voce e maior de idade pode consumir bebidas alcoolicas')

    bebidas = []
for i in range (3):
    bebida = input('digite uma bebida alcoolicas que voce gosta: ')
    bebidas.append(bebida) 
print(bebidas)
print('as bebidas que voce gosta sao:')
for bebida in bebidas:
    print(bebida)

    