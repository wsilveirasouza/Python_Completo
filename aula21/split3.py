'''
SPLIT - Exercício 3
'''
string = 'o brasil é o pais do futebol, o brasil é penta.'
lista1 = string.split(' ')
lista2 = string.split(',')

for valor in lista2:
    print(valor.strip().capitalize())
    