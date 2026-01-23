#os principaos operadores logicos em Python sao: and, or, not
# operador and retorna True se ambos os operandos forem True, caso contrario retorna False
# operador or retorna True se pelo menos um dos operandos for True, caso contrario retorna False
# operador not inverte o valor booleano do operando, ou seja, se for True retorna False e vice-versa

#exemplo and
idade = 20
altura = 1.75

resultado = (idade >= 18) and (altura >= 1.60)  # verifica se a pessoa e maior de idade e tem altura suficiente     
mensagem = "Pode entrar no parque."  + str(resultado)
print(mensagem)  # resultado: Pode entrar no parque. True

#exemplo or

temperatura = 30
resultado = (temperatura < 0) or (temperatura > 25)  # verifica se a temperatura esta fora do intervalo de 0 a 25 graus
mensagem = "A temperatura esta fora do intervalo ideal." + str(resultado)   
print(mensagem)  # resultado: A temperatura esta fora do intervalo ideal. True

#exemplo not
chovendo = False
resultado = not chovendo  # inverte o valor de chovendo     
mensagem = "Nao esta chovendo: " + str(resultado)
print(mensagem)  # resultado: Nao esta chovendo: True

#combinacao de operadores logicos
idade = 25
renda = 3000
resultado = (idade >= 18) and ((renda >= 2000) or (renda <= 5000))  # verifica se a pessoa e maior de idade e tem renda entre 2000 e 5000
mensagem = "Pode solicitar o emprestimo: " + str(resultado)
print(mensagem)  # resultado: Pode solicitar o emprestimo: True
# lembre-se de usar parenteses para agrupar as condicoes e garantir a ordem correta de avaliacao.
# operadores logicos sao muito uteis em estruturas de controle de fluxo, como if, while e for, para tomar decisoes com base em multiplas condicoes.


