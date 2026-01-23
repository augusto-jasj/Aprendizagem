# operadores de comparacao sao usados para comparar dois valores e retornam um valor booleano (True ou False)   
# == verifica se dois valores sao iguais
# != verifica se dois valores sao diferentes    
# > verifica se o valor da esquerda e maior que o valor da direita
# < verifica se o valor da esquerda e menor que o valor da direita
# >= verifica se o valor da esquerda e maior ou igual ao valor da direita
# <= verifica se o valor da esquerda e menor ou igual ao valor da direita

a = 10
b = 5
print(a == b)  # False, pois 10 nao e igual a 5
print(a != b)  # True, pois 10 e diferente de 5     
print(a > b)   # True, pois 10 e maior que 5
print(a < b)   # False, pois 10 nao e menor que 5
print(a >= b)  # True, pois 10 e maior ou igual a 5
print(a <= b)  # False, pois 10 nao e menor ou igual a
# Exemplo com strings
str1 = "hello"
str2 = "world"
print(str1 == str2)  # False, pois "hello" nao e igual a "world"
print(str1 != str2)  # True, pois "hello" e diferente de "
print(str1 < str2)   # True, pois "hello" vem antes de "world" na ordem lexicografica
print(str1 > str2)   # False, pois "hello" nao vem depois de "world" na ordem lexicografica
# Comparacao com booleanos
bool1 = True
bool2 = False
print(bool1 == bool2)  # False, pois True nao e igual a False
print(bool1 != bool2)  # True, pois True e diferente de False
print(bool1 > bool2)   # True, pois True e considerado maior que False
print(bool1 < bool2)   # False, pois True nao e considerado menor que False
# Comparacao entre diferentes tipos de dados
print(10 == 10.0)  # True, pois o valor numerico e igual
print(10 != "10")  # True, pois um e numero e o outro e string
print(5 > "3")     # TypeError, nao e possivel comparar int com str     
print("5" < 10)    # TypeError, nao e possivel comparar str com int
print(3.5 >= 3)    # True, pois 3.5 e maior que 3
print(4 <= 4.0)    # True, pois o valor numerico e iguaal 
# Lembre-se que ao comparar diferentes tipos de dados, pode ocorrer um erro de tipo (TypeError) se a comparacao nao for suportada entre os tipos envolvidos.

