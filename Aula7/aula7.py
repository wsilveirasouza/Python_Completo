"""
    Formatação
"""

nome = 'Wellington S de Souza'
idade = 32
altura = 1.75
e_maior = idade > 18
peso = 97
imc = peso / altura ** 2


print(nome, 'tem', idade, 'idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
# Formatando a forma que vai ser apresentado
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
# Formatando para exibir na ordem que eu quero
print('{2:.2f} {0} {0} tem {1} anos e seu imc é {2:.2f}'.format(nome, idade, imc))
# Parametros nomeados
print('{n} tem {i} anos de idade e seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))