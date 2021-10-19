'''
SPLIT, JOIN, ENUMERATE;
SPLIT - dividir uma string # str
JOIN - juntar uma lista # str
ENUMERATE - enumerar elementos da lista # iteráveis
'''
string = 'o brasil é o pais do futebol, o brasil é penta.'
lista1 = string.split(' ')
lista2 = string.split(',')

for valor in lista1:
    print(f'a palavra {valor} apareceu {lista1.count(valor)}x na frase.')

#print(lista1)
#print(lista2)
