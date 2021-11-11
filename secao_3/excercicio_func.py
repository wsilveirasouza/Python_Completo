'''
1 - CRIE UMA   FUNÇÃO1 QUE RECEBE UMA FUNÇÃO2 COMO PARÂMETRO E RETORNE O VALOR DA FUNÇÃO2 EXECUTADA.
'''

def ola_mundo():
    return 'Olá Mundo!'

def mestre(funcao):
    return funcao()

executando = mestre(ola_mundo)

print(executando)

'''
2 - CRIE UMA FUNÇÃO1 QUE RECEBE UMA FUNÇÃO2 COMO PARÂMETRO E RETORNE O VALOR DA FUNÇÃO2 EXECUTADA. FAÇA A FUNÇÃO1
EXECUTAR DUAS FUNÇÕES QUE RECEBAM UM NUMERO DIFERENTE DE ARGUMENTOS.
'''

def mestres(funcaoo, *args, **kwargs):
    return funcaoo(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executandos = mestres(fala_oi, 'TON')
executando2 = mestres(saudacao, 'Wellington', saudacao='Boa tarde!')

print(executandos)
print(executando2)

