# for ITEM in SEQUENCIA:
#for significa em portugues para
# item e uma variavel que vai receber cada elemento da sequencia a cada iteracao do laco
# sequencia pode ser uma lista, tupla, string ou qualquer objeto iteravel       

# exemplo com lista

lista = [2,3,4,6,7,8,0,9] # e uma lista de numeros 
for item in lista: # item e apenas uma variavel voce pode usar qualquer nome
    print(f'item da lista: {item}') 

# exemplo com string
palavras = 'Jose ' # eu criei uma string com o nome jose
for letra in palavras: # para cada letra na palavra eu vou imprimir a letra
    print(letra)

# range (valor_inicial, valor_final, incremento)  o valor final nao entra
#range(1,10) # vai de 1 a 9
#range(2,20,2) # vai de 2 a 18 pulando de 2 em 2
#range(1,10,2) # vai de 1 a 9 pulando de 2 em 2
# tambem existe o decremento
#range(10,1,-1) # vai de 10 a 2 pulando de 1 em 1 para tras
#range(20,2,-2) # vai de 20 a 4 pulando de 2 em 2 para tras

for x in range(1,10,2): # exemplo de range com incremento de 2
    print(f'valor de x com incremento de 2: {x}')

for numero in range(1,15): # range significa que intervalo de numeros de 1 a 14 o 15 nao entra
    print(f"Numero: {numero}")
    print("Fim do laço for")


for numero in range (10): # se eu colocar so o 10 ele vai do 0 ao 9 outro exemplo de range
    print(f'nuemero:{numero}')


# funcap range e muito util para gerar sequencias de numeros de forma simples e eficiente 
# a funcao range pode receber ate tres argumentos: inicio, fim e passo  

for numero in range(1, 6):  # range(inicio, fim) - fim é exclusivo
    print(f"Numero: {numero}")
    print("Fim do laço for")

nome = input("digite seu nome:") # usei input para a pesssoa digitar o nome dela
for x in range(10): # "o x comeca em 0 "o x e uma variavel de valor temporario que vai de 0 a 9  por que o range e 10
    print(f'{x+1} {nome}') #vai aparecer na tela o nome da pessoa 10 vezes com a contagem de 1 a 10 por que eu somei 1 ao x que comeca em 0

#vamos fazer outro exemplo
# eu nao quero que o quatzo seja repetido

pedras = ("Ametista", "Citrino", "Quartzo Rosa", "Olho de Tigre", "Turmalina Negra") # vou fazer uma lista usando tupla() de pedras
for pedra in pedras: # para cada pedra na lista de pedras eu vou imprimir o nome da pedra
    print(f'Pedra: {pedra}') # o quartzo estara sendo impresso


pedras = ("Ametista", "Citrino", "Quartzo Rosa", "Olho de Tigre", "Turmalina Negra") 
for pedra in pedras:
    if pedra == "Quartzo Rosa": # se a pedra for quartzo rosa eu vou pular essa iteracao
        continue # o continue pula a iteracao atual e vai para a proxima
    print(f'Pedra: {pedra}')