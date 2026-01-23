for cont_ex in range(1,6): # eu quero pegar o nmr de 1 a 5
    print(f'contagem ex:{cont_ex}')
    for cont_interno in range(5,0,-1): # eu pegar primero o numero 5 e vou ate o 1
        print(f'contagem interno:{cont_interno}')

print("fim do laco ")

#outro exemplo de laco for 

import random  # importando o modulo random para gerar numeros aleatorios

for A in range(1,6):# eu quero rodar 5 vezes emtao vai ser de 1 a 6
    print(F'\ncontagem:{A}')
    for b in range(5):
        num = random.randint(1,100) # gerando um numero aleatorio entre 1 e 100. O random significa que e um numero inteiro e randint e a funcao que gera o numero aleatorio entao random.randint(1,100)vai gerar numeros aleatorios de 1 a 100
        print(f'numero aleatorio:{num}')    
