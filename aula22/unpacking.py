'''
Desempacomento de listas
'''
lista = ['Luiz','Joao','Maria',1,2,3,4,5,6,7,8,9,100]
# *_ significa que não será utilizado no restante do código
n1, n2, n3, *outra_lista, ultimo_da_lista = lista

print(n1, n2, n3, outra_lista, ultimo_da_lista)
