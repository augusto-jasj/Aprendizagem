# condiconais if, elif, else

# simples , composto, encadeado

nota_1 = nota_2 = 0.0

media = 0.0

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

# calcular a media
media = (nota_1 + nota_2) / 2

if media >= 7.0: # if se a media for maior ou igual a 7.0 aluno passa
    print("Aluno aprovado :", media)
    print("Parabens!")
elif media >= 5.0: # se a media for maior ou igual a 5.0 e menor que 7.0 aluno esta em recuperacao
    print("Aluno em recuperacao :", media)
    print("Estude mais!")
else:   # se a media for menor que 5.0 aluno reprovado
    print("Aluno reprovado :", media)
    print("Estude mais!")

print(" sua media e {}".format(media)) #.format para formatar a saida e a {} e um placeholder para o valor da media placeholder e um espaco reservado para um valor que sera inserido posteriormente

    
# vimos como trabalhar com estruturas condicionais usando if, elif e else para tomar decisoes com base em condicoes diferentes.