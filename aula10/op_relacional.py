"""
    Operadores Relacionais
    == igualdade
    > maior que
    >= maior que ou igual a
    < menor que
    <= menor que ou igual a
    != diferente de
"""

# print(2 == 2)
#
# print(2 > 1)
# print(2 > 2)
#
# print(2 >= 1)
# print(2 >= 2)
# print(2 >= 3)
#
# print(2 < 3)
# print(2 < 1)
#
# print(2 <= 1)
# print(2 <= 2)
# print(2 <= 3)
#
# print(2 != 1)
# print(2 != 2)

# nome = input('Qual o seu nome? ')
# idade = int(input('Qual a sua idade? '))
#
# # Limite para empréstimo
# idade_menor = 20
# idade_maior = 30
#
# if idade >= idade_menor and idade <= idade_maior:
#     print(f'{nome} pode pegar o empréstimo.')
# else:
#     print(f'{nome} NÃO PODE PEGAR O EMPRÉSTIMO!')

nome = 'Joãozinho'
idade = """40"""
peso = 80.5
e_maior = True
idade = int(idade)

if idade > 18:
    print(f'{nome} é maior de idade.')
else:
    print(f'{nome} NÃO é maior de idade.')
