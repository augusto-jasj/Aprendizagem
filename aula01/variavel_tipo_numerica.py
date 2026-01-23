media = 0 
n1 = n2 = n3 = n4 = 0.0  # variaveis do tipo numerica sao usadas para armazenar valores numericos, como inteiros e numeros de ponto flutuante.

nome, idade, altura = "Maria", 22, 1.68  # exemplo de variaveis com diferentes tipos de dados, elas sao diferentes numero e texto ai nos separamos por virgulas

estado_civil = True  # variavel booleana armazena valores de verdadeiro ou falso ele so pode assumir esses dois valores

#funcao type() e usada para verificar o tipo de dado armazenado em uma variavel.
print(type(media))
print(type(n1))
print(type(nome))
print(type(estado_civil))
print(type(1+3j)) # exemplo de numero complexo e um tipo numerico que representa numeros na forma a + bi, onde a e b sao numeros reais e i e a unidade imaginaria.

#funcao isinstance() e usada para verificar se uma variavel e de um determinado tipo de dado. Ela retorna dados verdadeiro oou falso se a variavel for do tipo especificado.
a = 10
b = "Hello"
c = 3.14

print(isinstance(a, int))  # verifica se a e um inteiro
print(isinstance(b, str))  # verifica se b e uma string 
print(isinstance(c, float))  # verifica se c e um numero de ponto flutuante
print(isinstance(a,( int , float)))  # verifica se a e um inteiro ou float

a = 5
c = 2
r = a * c 
print(r) # as variaveis sao flexiveis e podem ser usadas em operacoes matematicas como multiplicacao, adicao, subtracao e divisao. E as variaveis podem ter os valores reatribuidos







