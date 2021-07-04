"""
Faça um programa que peça o primeiro nome do usuário.
Se o nome tiver 4 letras ou menos escreva “Seu nome é curto”;
se tiver entre 5 e 6 letras, escreva “Seu nome é normal”;
maior que 6 escreva “Seu nome é muito grande”.
"""

nome = input('Digite o seu nome: ')
carcter_nome = len(nome)

if carcter_nome <= 4:
    print('Seu nome é muito curto! ')
elif carcter_nome >= 5 and carcter_nome <= 6:
    print('Seu nome é normal! ')
elif carcter_nome > 6:
    print('Seu nome é muito grande! ')
else:
    print('Valor inválido! ')