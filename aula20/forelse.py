
'''
FOR ELSE    
'''
variavel = ['wellington','matheus','lucas']

for valor in variavel:
    if valor.lower().startswith('j'):
        pass
        # continue
    print(valor)
else:
    print('nao existe uma palavra que começa com a letra j.')