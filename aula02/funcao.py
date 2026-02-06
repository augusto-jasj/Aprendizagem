# o que e uma funcao? uma funcao e um bloco de codigo que realiza uma tarefa especifica, e pode ser reutilizado em diferentes partes do programa. funcoes sao definidas usando a palavra-chave def, seguida pelo nome da funcao e parenteses. o codigo da funcao deve ser indentado, ou seja, deve estar recuado em relacao a linha de definicao da funcao. funcoes podem receber parametros, que sao valores que podem ser passados para a funcao quando ela e chamada. funcoes podem retornar valores, ou seja, podem produzir um resultado que pode ser usado em outras partes do programa. a sintaxe basica para definir uma funcao e:
#modularizacao, reuso de codigo e a legibilidade do codigo sao algumas das vantagens de usar funcoes em um programa. funcoes permitem que o codigo seja organizado em blocos logicos, facilitando a leitura e a manutencao do codigo. alem disso, funcoes permitem que o codigo seja reutilizado em diferentes partes do programa, evitando a duplicacao de codigo e tornando o programa mais eficiente. funcoes tambem permitem que o codigo seja testado de forma isolada, facilitando a identificacao e correção de erros.   

#entrada ----> funcao ----> saida

#existem 2 funcoes built-in em python: print() e input(). a funcao print() e usada para exibir mensagens na tela, enquanto a funcao input() e usada para ler dados do usuario. ambas as funcoes sao muito importantes para a interacao do usuario com o programa, e sao amplamente utilizadas em programas python. a funcao print() pode receber um ou mais argumentos, que podem ser de qualquer tipo de dado, e os exibe na tela. a funcao input() recebe uma string como argumento, que e exibida como um prompt para o usuario, e retorna a entrada do usuario como uma string. ambas as funcoes sao essenciais para a comunicacao entre o programa e o usuario, permitindo que o programa receba dados do usuario e forneca feedback de forma clara e eficiente.
# def significa definir uma funcao, ou seja, criar um bloco de codigo que realiza uma tarefa especifica e pode ser reutilizado em diferentes partes do programa. a sintaxe basica para definir uma funcao e:    
#def < nome_funcao> ( <parametros> ):
#    <bloco de codigo>

def mensagem():
    print('ola mundo')
    print("Olá, esta é uma mensagem de exemplo!") # isso vai imprimir a mensagem "Olá, esta é uma mensagem de exemplo!" na tela quando a funcao for chamada

mensagem()

# funcao com argumentos
def soma(a,b):
    print(a + b)

soma(123,435)# isso vai imprimir 558, pois a funcao soma recebe os argumentos 123 e 435, e imprime a soma desses dois numeros na tela. a funcao soma realiza a operacao de adicao entre os dois argumentos e exibe o resultado usando a funcao print(). quando chamamos soma(123,435), o valor de a e 123 e o valor de b e 435, entao a funcao calcula 123 + 435 e imprime o resultado, que e 558.  



def mult (x,b):
    return x * b  # return e usado para retornar um valor da funcao, ou seja, para produzir um resultado que pode ser usado em outras partes do programa. quando a funcao mult e chamada, ela recebe os argumentos x e b, realiza a operacao de multiplicacao entre eles, e retorna o resultado usando a palavra-chave return. o valor retornado pela funcao pode ser armazenado em uma variavel ou usado diretamente em outras partes do programa. por exemplo, podemos chamar a funcao mult(5,10) e armazenar o resultado em uma variavel chamada resultado, como resultado = mult(5,10). isso vai calcular 5 * 10 e armazenar o valor 50 na variavel resultado. podemos entao imprimir o valor de resultado usando print(resultado), que vai exibir 50 na tela. a palavra-chave return permite que a funcao produza um resultado que pode ser utilizado em outras partes do programa, tornando a funcao mais flexivel e reutilizavel.    

a = 4
b = 5
c = mult(a,b)
print(c) # isso vai imprimir 20, pois a funcao mult recebe os argumentos a e b, que tem os valores 4 e 5 respectivamente, realiza a operacao de multiplicacao entre eles, e retorna o resultado usando a palavra-chave return. o valor retornado pela funcao mult e 20, que e armazenado na variavel c. quando chamamos print(c), o valor de c, que e 20, e exibido na tela. entao a funcao mult(4,5) calcula 4 * 5 e retorna 20, que e armazenado em c e impresso na tela. 

def div(k,j):
    return k / j
if __name__ == "__main__":
    a = int(input("Digite o valor de k: "))
    b = int(input("Digite o valor de j: "))
    r = div(a,b)
    print(f"O resultado da divisão de {a} por {b} é: {r}") # isso vai solicitar ao usuario que digite os valores de k e j, chamar a funcao div com esses valores, e imprimir o resultado da divisao na tela. a condicao if __name__ == "__main__": garante que o codigo dentro desse bloco seja executado apenas quando o script for executado diretamente, e nao quando for importado como um modulo em outro script. isso permite que a funcao div seja reutilizada em outros scripts sem executar o codigo de entrada e saida. quando o usuario digitar os valores de k e j, a funcao div sera chamada com esses valores, e o resultado da divisao sera calculado e impresso na tela usando uma f-string para formatar a mensagem de saida.  




def div (k,j):
    if j == 0:
        return "Erro: Divisão por zero não é permitida."
    else:
        return k / j # isso vai retornar o resultado da divisao de k por j se j for diferente de zero. se j for igual a zero, a funcao retorna uma mensagem de erro indicando que a divisao por zero nao e permitida. isso evita erros de runtime e fornece feedback claro ao usuario sobre o motivo da falha na operacao de divisao.   

if __name__ == "__main__":
    a = int(input("Digite o valor de k: "))
    b = int(input("Digite o valor de j: "))
    r = div(a,b)
    print(f"O resultado da divisão de {a} por {b} é: {r}")