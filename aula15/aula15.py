"""
    FOrmatando valores com modificadores - Aula 5
    :s = Texto (strings)
    :d = Inteiros (int)
    :f = Números de ponto flutuante (float)
    :.(NÚMERO)f - Quantidade de casas decimais (float)
    :(CARACTERE) (> ou < ou ^) (QUantidade) (TIPO - s, d ou f)

    > - Esquerda
    < - Direita
    ^ - Centro
"""

num1 = 1325
num2 = 1150
num3 = 3553

print(f'{num1:0>10}')
print(f'{num2:0<10}')
print(f'{num3:0^10}')

print(f'{num1:.3f}')

nome = 'wellington'
sobrenome = 'Souza'
nome_f = '{:@^12} {:#>10}'.format(nome, sobrenome)
print(nome_f)


nome2 = 'Silveira'
print(nome2.lower()) # Minúscula
print(nome2.upper()) # Maiúscula
print(nome2.title()) # Primeira maiúscula
print(nome2.ljust(20,'@')) # Justifica com o caractere informado

