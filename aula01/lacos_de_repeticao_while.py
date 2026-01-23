# o que e um laco de repeticao while em python
# estrutura de repeticao while

#num = 1

#while (num <=10):
#    print(num)

# aqui temos um laço infinit mas eu quero que imprima do 1 ao 10    

num = 1

while (num <= 10):
    print(num)
    num +=1 # ele vai somar 1 a variavel num a cada repeticao do laco ate que chegue a 10 
    print("fim do laco")

    #while significa enquanto, ou seja, enquanto a condicao for verdadeira o laco continua executando
#num = num + 1  mesma coisa que num +=1
# aprendemos a usar a estrutura de repeticao while para executar um bloco de codigo enquanto uma condicao for verdadeira.
# vimos como controlar o fluxo do laco usando uma variavel de controle e como evitar laco infinito.
# tambem aprendemos a indentacao correta do codigo dentro do laco while.

#vamos fazer outro exemplo mas nos nao sabemos quantas vezes o laco vai repetir

nome = None #  None signivica que a variavel nao tem valor vazia nao tem nada

while True :
    print("Digite seu nome: ")
    nome =  input()  # lendo o nome do usuario
    if nome == 'x' or nome == 'X':  # verificando se o usuario quer sair usamos x ou X usamos x minusculo e maiusculo para nao ter erro de clicar em um diferente
        break  # sai do laco se o usuario digitar x ou X o brak interrompe o laco imediatamente ela nao finaliza o if e sim o laco while

    print(f'seja bem vindo,{nome}')
print("fim do programa")

# nesse exemplo usamos um laco infinito com while True e dentro do laco verificamos se o usuario quer sair digitando x ou X.
# se o usuario digitar x ou X usamos a instrucao break para sair do laco imediatamente.
# caso contrario, saudamos o usuario com uma mensagem personalizada.    

