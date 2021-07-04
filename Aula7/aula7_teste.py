"""
    Teste de formatação
        Criar variaveis para nome (str), idade (int)
        Altura (float) e peso (float) de uma pessoa
        Criar variavel com o ano atual (int)
        Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
        Obter o imc da pessoa com 2 casas decimais (peso e na altura da pessoa)
        Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome = 'Wellington'
idade = 39
altura = 1.75
ano_atual = 2021
ano_nasc = ano_atual - idade
peso = 97
imc = peso / altura ** 2

# Formatando com f strings
print(f'{nome} tem {idade} anos, {altura:.2f} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {ano_nasc}.')

# Formatando com parametrização
print('{n} tem {i} anos, {alt:.2f} de altura e pesa {p}kg.'.format(n=nome, i=idade, alt=altura, p=peso))
print('O IMC de {n} é {im:.2f}.'.format(n=nome, im=imc))
print('{n} nasceu em {an}.'.format(n=nome, an=ano_nasc))

"""
print('{n} nasceu em {aa} tem {i} anos de idade seu imc é {im:.2f} pesa {p:.2f} kilos e sua altura é {alt:.2f}.'
      .format(n=nome, aa=ano_nasc, i=idade, p=peso, alt=altura, im=imc))
"""
