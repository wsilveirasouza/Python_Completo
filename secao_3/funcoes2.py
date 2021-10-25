'''
FUNÇÕES (def) em Python - return
'''
def funcao(var):
    return var
    # print(var)

variavel = funcao('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor.')

# tratamento de exceções
def divisao(n1, n2):
    if n1 > 0 and n2 > 0:
        return n1 / n2
    else:
        print('Conta inválida.')

divide = divisao(8,0)

print(divide)