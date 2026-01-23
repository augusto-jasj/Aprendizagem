# modulos sao importados em python usando a palavra-chave import
# modulos sao arquivos python que contêm definições e instruções que podem ser reutilizadas em outros programas python  
# no site do python https://docs.python.org/3/pt-br/library/ voce encontra a lista completa de modulos padroes disponiveis em python
# para instalar modulos adicionais, voce pode usar o gerenciador de pacotes pip
# por exemplo, para instalar o modulo requests, voce pode usar o comando: pip install requests
# depois de instalar o modulo, voce pode importá-lo no seu codigo python e usar suas funcionalidades
# para usar um modulo, voce precisa importá-lo no seu código usando a palavra-chave import seguida do nome do modulo


import math # modulo de funcoes matematicas
print(math.sqrt(16)) # usando a funcao sqrt do modulo math para calcular a raiz quadrada de 16

# eu sempre precio importar o modulo antes de usar suas funcoes
#podemos fazer FROM para importar apenas uma funcao especifica do modulo
from math import sqrt  # importando apenas a funcao sqrt do modulo math

print(sqrt(25))  # usando a funcao sqrt diretamente sem precisar do prefixo math.
# aprendemos a importar modulos em python usando a palavra-chave import.

# tambem podemos usar o import universal para importar todas as funcoes de um modulo
from math import *  # importando todas as funcoes do modulo math tome muito cuidado com isso pois pode gerar conflitos de nomes

#podemos usar tambem  o modulo math mas eu quero que ele seja mais curto
import math as m  # importando o modulo math com um alias m

# e podemos usar nossos proprios modulos
import lacos_de_repeticao_while 

# e para encurtar iremos usar ldrw
import lacos_de_repeticao_while as ldrw

# __name__ == "__main__":
if __name__ == "__main__":
    print("Este modulo esta sendo executado diretamente")
# __name__ e uma variavel especial em python que indica se o modulo esta sendo executado diretamente ou importado por outro modulo e __main__ e o nome do modulo principal quando executado diretamente 
# entao podemos usar essa verificacao para executar codigo apenas quando o modulo for executado diretamente
# futuramente explicarei melhor sobre isso


