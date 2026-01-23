#sintaxe 
# print("texto, argumentos") 

mensagem =' funcao print em python()'
print(mensagem)  # exibindo a mensagem na tela
print("A mensagem e:", mensagem)  # exibindo a mensagem com texto adicional 

nome = "Carlos"
idade = 28
print("Nome:", nome, "Idade:", idade)  # exibindo multiplos valores separados por virgula
# usando format para formatar a saida
print("Nome: {} Idade: {}".format(nome, idade))  # usando format para formatar a saida
# usando f-strings para formatar a saida (disponivel a partir do Python 3.6)        
print(f"Nome: {nome} Idade: {idade}")  # usando f-strings para formatar a saida
# formatando numeros com f-strings      
preco = 49.99
print(f"Preco: R$ {preco:.2f}")  # formatando o numero com duas casas decimais
# alinhamento de texto com f-strings        
produto = "Camisa"
print(f"Produto: {produto:<10} Preco: R$ {preco:.2f}")  # alinhando o texto a esquerda com largura de 10 caracteres
print(f"Produto: {produto:>10} Preco: R$ {preco:.2f}")  # alinhando o texto a direita com largura de 10 caracteres
print(f"Produto: {produto:^10} Preco: R$ {preco:.2f}")  # alinhando o texto ao centro com largura de 10 caracteres
# preenchendo com caracteres especiais  
print(f"Produto: {produto:*<10} Preco: R$ {preco:.2f}")  # preenchendo com asteriscos a esquerda
print(f"Produto: {produto:*>10} Preco: R$ {preco:.2f}")  # preenchendo com asteriscos a direita
print(f"Produto: {produto:*^10} Preco: R$ {preco:.2f}")  # preenchendo com asteriscos ao centro 

print(f'produto: {produto: -------<10} Preco: R$ {preco:.2f}')  # preenchendo com traços a esquerda
print(f'produto: {produto: -------^10} Preco: R$ {preco:.2f}')  # preenchendo com traços ao centro
print(f'produto: {produto: -------^10} Preco: R$ {preco:.2f}')  # preenchendo com traços a direita  

  
print("imprime e muda de linha")
print("imprime a mensagem e nao muda de linha", end="") # o end="" faz com que a funcao print nao mude de linha apos imprimir a mensagem
print("continuacao da mensagem na mesma linha")

nome_usuario = 'maria'
idade = 22
msg = 'o nome dela e {0} e ela tem {1}anos'.format(nome_usuario,idade)
print(msg)

# aprendemos a usar a funcao print para exibir mensagens e valores na tela, incluindo diferentes tecnicas de formatacao.
# tambem vimos como controlar o comportamento da funcao print usando o parametro end.
# aprendemos a usar a funcao print para exibir mensagens e valores na tela, incluindo diferentes tecnicas de formatacao.
# tambem vimos como controlar o comportamento da funcao print usando o parametro end.

a = 19
b = 23
print(f'o valor de a e {a} e o valor de b e {b}')

valor = 1234.56789
print (f'o valor e {valor:.2f}') #aqui dentro do valor eu quero so 2 casas decimais :.2f signfica duas casas decimais float

valor = 1234.56789
print (f'o valor e \'{valor:.2f}\'') #aqui dentro do valor eu quero so 2 casas decimais :.2f signfica duas casas decimais float e estamos usando \ \'' para colocar aspas simples na saida
print (f'o valor e \"{valor:.2f}\"') #aqui dentro do valor eu quero so 2 casas decimais :.2f signfica duas casas decimais float e estamos usando \ \"\" para colocar aspas duplas na saida

nome = 'Ana'
idade = 30
print(f'nome:{nome} idade:{idade}') # vai ficar sem espaco entre nome e idade

print(f'nome:{nome}\t idade:{idade}') # \t e um caractere especial que representa uma tabulacao, ou seja, um espaco maior entre os elementos
print(f'nome:\t{nome}\t idade:\t{idade}') # outro exemplo de uso do \t para tabulacao

