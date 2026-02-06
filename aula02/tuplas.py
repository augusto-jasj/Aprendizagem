#tuplas sao imutaveis, ou seja, nao podem ser alteradas depois de criadas
#sao criadas usando parenteses
#tuplas podem conter elementos de tipos diferentes
#tuplas sao indexadas, ou seja, podemos acessar seus elementos usando indices

tupla = (2,2,2,2,2,3,34,)
tupla[1]= 5 # isso vai gerar um erro, pois tuplas sao imutaveis
print(tupla)

simbolos_quimicos = ("H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne")
print(len(simbolos_quimicos))

print(simbolos_quimicos[0:3] )

print('c'in simbolos_quimicos)

print(sum(tupla))

#operacoes nao disponiveis para tuplas: append, extend, insert, remove, pop, clear, sort, reverse todo metodo que altera a tupla nao esta disponivel, pois tuplas sao imutaveis

for elemento in simbolos_quimicos:
    print(f'elemento: {elemento}')


grupo = list("H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne")
print(grupo)
# agora podemos usar os metodos de lista para alterar o grupo, como append, extend, insert, remove, pop, clear, sort, reverse
grupo.append("Na")
print(grupo)

grupo1 = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne"]
alcalinos = tuple(grupo1)
print(alcalinos)
# transformamos a lista em tupla, agora nao podemos mais alterar a tupla, mas podemos acessar seus elementos usando indices
print(sorted(alcalinos)) # sorted retorna uma nova lista ordenada, mas a tupla original permanece inalterada

