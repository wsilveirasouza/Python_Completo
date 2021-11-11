'''
EXPRESSÕES: lambda são FUNÇÕES: anônimas
'''
# def funcao(arg, arg2):
#     return arg * arg2
#
# var = funcao(2,2)
# print(var)
#
# # Escrevendo em lambda
# a = lambda x, y: x * y
# print(a(2,2))

# exemplo 2
# criando uma lista
lista = [
    ['p1', 13],
    ['p2', 6],
    ['p3', 25],
    ['p4', 12],
    ['p5', 38],
    ['p6', 50],
]
# # função que ordena itens
# def ordena_item(item):
#     return item[1]
# # ordenar listas
# lista.sort(key=ordena_item, reverse=True) # reverse: ordena inversamente a lista
# print(lista)
# lista.sort(key=lambda item: item[1], reverse=False)
# print(lista)
print(sorted(lista, key=lambda i: i[1], reverse=True))
