'''
FOR ELSE
'''
variavel = ['joao','pedro','wellington']

for valor in variavel:
    print(valor)
    if valor.lower().startswith('j'):
        break
    else:
        print('nao existe uma palavra que começão com j.')
