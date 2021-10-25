'''
Funções - def em Python (parte 1)
'''
def saudacao(msg='Olá', nome='usuário'):
    # Trocando a letra 'e' pelo 3
    nome = nome.replace('e','3')
    msg = msg.replace('e','3')
    return f'{msg} {nome}'
    # print(msg, nome)

# Passando parametros
#saudacao('Olá', 'Wellington')
#saudacao(nome='World')
#saudacao(nome='Jackson', msg='Bye!')
variavel = saudacao()

print(variavel)
