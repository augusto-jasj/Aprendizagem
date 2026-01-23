# operadores aritimeticos sao usados para realizar calculos matematicos
# + e usado para adicao
# - e usado para subtracao  
# * e usado para multiplicacao
# / e usado para divisao
# // e usado para divisao inteira (retorna o quociente sem a parte decimal)
# % e usado para obter o resto de uma divisao
# ** e usado para exponenciacao (eleva um numero a uma potencia)

# ordem de precedencia dos operadores aritimeticos:
# 1. parenteses ()
# 2. exponenciacao (**)
# 3. multiplicacao (*), divisao (/), divisao inteira (//), resto
# 4. adicao (+), subtracao (-)
# operadores com a mesma precedencia sao avaliados da esquerda para a direita

x = y = z = 10 

x = 5 + 3 * 2  # multiplicacao e feita primeiro, depois a adicao
y = (5 + 3) * 2  # parenteses alteram a ordem de avaliacao, entao a adicao e feita primeiro
z = 10 % 3  # o resto da divisao de 10 por 3 e 1
print(x)  # resultado: 11
print(y)  # resultado: 16
print(z)  # resultado: 1    

n = o = m = 0

n = 3
o = 5

m = n + o 
print(m)  # resultado: 8


x = y = z = 0

x = input("Digite o primeiro numero: ")
y = input("Digite o segundo numero: ")  

z = int(x) + int(y)  # converte as entradas de string para inteiros antes de somar
print("A soma e:", z)  # exibe o resultado da soma

# tambem e possivel fazer dessa forma

x = int(input("Digite o primeiro numero: "))
y = int(input("Digite o segundo numero: "))
z = x + y
print("A soma e:", z)   
# lembre-se que a funcao input() sempre retorna uma string, entao e necessario converter para o tipo numerico apropriado (int ou float) antes de realizar operacoes aritimeticas.

