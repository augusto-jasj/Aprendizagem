#manipuçacao de strings
# strings sao imutaveis, ou seja, nao podem ser alteradas depois de criadas

frase = "Hello, World!"
letras = frase[2]
print(letras) # isso vai imprimir "l", pois o indice 2 da string "Hello, World!" é a letra "l"
print(len(frase)) # isso vai imprimir 13, pois a string "Hello, World!" tem 13 caracteres (contando o espaço e a pontuação)


user = 'jose ta aprendendo python'
frase = ' e esta gostando muito' 
juncao = user + frase
print(juncao) # isso vai imprimir "jose ta aprendendo python e esta gostando muito", pois estamos concatenando as duas strings usando o operador +

user = 'jose ta aprendendo python'
frase = user.split()
print(frase) # isso vai imprimir ['jose', 'ta', 'aprendendo', 'python'], pois o metodo split() divide a string em uma lista de palavras usando o espaço como separador
for palavra in frase:
    print(palavra) # isso vai imprimir cada palavra da lista em uma linha diferente

email  = input("digite seu email: ")
arroba = email.find("@") # para encontrar a posição do caractere "@" na string email
print(arroba) # isso vai imprimir a posição do caractere "@" na string email, ou seja, o indice onde ele se encontra. Se o caractere "@" nao for encontrado, o metodo find() retorna -1.
user = email[0:arroba]
dominio = email[arroba+1:]
print(user)
print(dominio) # isso vai imprimir o nome de usuario e o dominio do email, separados pelo caractere "@". O nome de usuario é a parte da string email que vai do indice 0 até o indice do caractere "@", e o dominio é a parte da string email que vai do indice do caractere "@" + 1 até o final da string email.


produtos = 'celular, notebook, tablet, fone de ouvido'
print('sodio' in produtos) # isso vai imprimir False, pois a palavra "sodio" nao esta presente na string produtos
print('notebook' in produtos) # isso vai imprimir True, pois a palavra "notebook" esta presente na string produtos
print('mag'not in produtos) # isso vai imprimir False, pois a palavra "mag" nao esta presente na string produtos, mesmo que a palavra "notebook" esteja presente, a palavra "mag" nao esta presente, pois ela nao é uma substring da string produtos    

item= 'hipon'
pos = item.find('hin')
print(pos) # isso vai imprimir 2, pois a substring "hin" começa no indice 2 da string "hipon". Se a substring nao for encontrada, o metodo find() retorna -1.
pos = item.find('abc')
print(pos) # isso vai imprimir -1, pois a substring "abc" nao esta presente na string "hipon". O metodo find() retorna -1 quando a substring nao é encontrada na string.


obj = 'galaxia Espiral Milky Way'
print(obj.upper()) # isso vai imprimir "GALAXIA ESPIRAL MILKY WAY", pois o metodo upper() converte todos os caracteres da string para maiusculo
print(obj.lower()) # isso vai imprimir "galaxia espiral milky way", pois o metodo lower() converte todos os caracteres da string para minusculo
print(obj.title()) # isso vai imprimir "Galaxia Espiral Milky Way", pois o metodo title() converte a primeira letra de cada palavra para maiusculo e as demais letras para minusculo    
print(obj.capitalize()) # isso vai imprimir "Galaxia espiral milky way", pois o metodo capitalize() converte a primeira letra da string para maiusculo e as demais letras para minusculo    

suplemento = 'vitamina C'
novo_suplemento = suplemento.replace('vitamina C', 'zinco')
print(suplemento)
print(novo_suplemento) # isso vai imprimir "vitamina C" e "zinco", pois o metodo replace() substitui a substring "vitamina C" pela substring "zinco" na string suplemento, mas a string suplemento original permanece inalterada, pois strings sao imutaveis. O metodo replace() retorna uma nova string com as substituições realizadas.   

frase = '   Python é uma linguagem de programação muito popular.   '
print(frase)
print(frase.strip()) # isso vai imprimir "Python é uma linguagem de programação muito popular.", pois o metodo strip() remove os espaços em branco do inicio e do final da string frase, mas a string frase original permanece inalterada, pois strings sao imutaveis. O metodo strip() retorna uma nova string com os espaços em branco removidos. 
print(frase.lstrip()) # isso vai imprimir "Python é uma linguagem de programação muito popular.   ", pois o metodo lstrip() remove os espaços em branco do inicio da string frase, mas a string frase original permanece inalterada, pois strings sao imutaveis. O metodo lstrip() retorna uma nova string com os espaços em branco removidos do inicio da string.
print(frase.rstrip()) # isso vai imprimir "   Python é uma linguagem de programação muito popular.", pois o metodo rstrip() remove os espaços em branco do final da string frase, mas a string frase original permanece inalterada, pois strings sao imutaveis. O metodo rstrip() retorna uma nova string com os espaços em branco removidos do final da string.    


fruta = 'banana'
print(fruta)
print(fruta.rjust(10)) # isso vai imprimir "    banana", pois o metodo rjust() alinha a string fruta à direita, preenchendo os espaços em branco à esquerda da string com o caractere de preenchimento (por padrão, um espaço em branco) até que a string tenha o comprimento especificado (neste caso, 10). O metodo rjust() retorna uma nova string com a formatação aplicada.
print(fruta.ljust(10)) # isso vai imprimir "banana    ", pois o metodo ljust() alinha a string fruta à esquerda, preenchendo os espaços em branco à direita da string com o caractere de preenchimento (por padrão, um espaço em branco) até que a string tenha o comprimento especificado (neste caso, 10). O metodo ljust() retorna uma nova string com a formatação aplicada.
print(fruta.center(10)) # isso vai imprimir "  banana   ", pois o metodo center() centraliza a string fruta, preenchendo os espaços em branco à esquerda e à direita da string com o caractere de preenchimento (por padrão, um espaço em branco) até que a string tenha o comprimento especificado (neste caso, 10). O metodo center() retorna uma nova string com a formatação aplicada.  
print(fruta.center(10,'-')) # isso vai imprimir "--banana---", pois o metodo center() centraliza a string fruta, preenchendo os espaços em branco à esquerda e à direita da string com o caractere de preenchimento especificado (neste caso, um hífen) até que a string tenha o comprimento especificado (neste caso, 10). O metodo center() retorna uma nova string com a formatação aplicada.    


p = 'python'
print(p.startswith('py')) # isso vai imprimir True, pois a string p começa com a substring "py"
print(p.endswith('on')) # isso vai imprimir True, pois a string p termina com a substring "on"
print(p.startswith('Py')) # isso vai imprimir False, pois a string p nao começa com a substring "Py", pois a comparação é sensível a maiúsculas e minúsculas
print(p.endswith('On')) # isso vai imprimir False, pois a string p nao termina com a substring "On", pois a comparação é sensível a maiúsculas e minúsculas 


#docstrings
texto = '''
   docstrings e uma especia de documentacao que podemos inserir dentro  de um modulo funcao ou cllasse no py entre outros locais
    docstrings sao criadas usando tres aspas simples ou tres aspas duplas, e podem conter varias linhas de texto    

 '''

print(texto)





