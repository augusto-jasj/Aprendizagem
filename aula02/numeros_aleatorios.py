import random

valor = random.randint(1, 10) # Gera um número inteiro aleatório entre 1 e 10 randint em ingles significa "integer random" (número inteiro aleatório)
print("Número aleatório gerado:", valor)


print(' eu quero gerar numero aleatorio de 1 a 20')
for aleatorio in range (5):
    valor = random.randint(1, 20)
    print("Número aleatório gerado:", valor)

valor = random.random ()
print(f'numero aleatorio entre 0 e 1: {valor}')

valor = random.random() # Gera um número float aleatório entre 0.0 e 1.0
print(f'numero aleatorio : {valor * 10}')# Multiplica por 10 para obter um número entre 0 e 10

valor = random.random()
print(f'nuemero aleatorio : {round(valor * 10, 2)}') # Arredonda para 2 casas decimais pq eu add um 2 no round o round é uma função que arredonda um número para um número especificado de casas decimais

valor = random.uniform(1,10) # Gera um número float aleatório entre 1 e 10 ele e semelante ao randint mas para float
print(f'numero aleatorio: {round(valor, 4)}') # Arredonda para 4 casas decimais

lista = [10, 20, 30, 40, 50]
valor = random.choice(lista)# Escolhe um elemento aleatório da lista
print(f'numero aleatorio da lista: {valor}')

lista = [1, 2, 3, 4, 5]
n = random.sample(lista, 3) # Seleciona 3 elementos únicos da lista
print(f'3 numeros aleatorios da lista: {n}')    

lista = [1, 2, 3, 4, 5]
random.shuffle(lista) # Embaralha a lista colocando em uma ordem aleatória
print(f'lista embaralhada: {lista}')    
