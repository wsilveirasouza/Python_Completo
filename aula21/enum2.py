'''
Função: ENUMERATE
Retorna Tuplas
'''
lista = [
    [0,'Well'], [1,'Jana'], [2,'Filhos'],
]

for v in lista:
    print(v[0], v[1])

for indice, nome in lista:
    print(indice, nome)

lista1 = ['Lala','Pedro','Dener']

for indice, nome in enumerate(lista1):
    print(indice, nome)