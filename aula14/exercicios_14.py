"""
    Faça um programa que peça ao usuário para digitar um número inteiro,
    informe se este número é par ou ímpar.
    Caso o usuário não digite um número inteiro,
    informe que não é um número inteiro.
"""

num1 = input('Digite um núnero inteiro: ')

try:
    num1 = int(num1)
    print('O valor digitado é inteiro.')
    if num1 % 2 == 0:
        print('O valor informado é PAR.')
    else:
        print('O valor informado é IMPAR.')
except:
    print('Valor inválido!')

