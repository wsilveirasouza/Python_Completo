'''
Função: ENUMERATE
Enumerar elementos de uma lista
'''

string = 'o brasil é o pais do futebol'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])
    