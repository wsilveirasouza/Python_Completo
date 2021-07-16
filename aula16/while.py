"""
Estruturas de repetição
WHILE
Utilizado para realizar ações enquanto
uma condição for verdadeira.
"""
# x = 0
# while x < 5:
#     print(x)
#     x = x + 1
#
# print('Acabou!')
# while x < 10:
#     if x == 3:
#         x = x + 1
#         continue # volta para o inicio do laço se a condição for True
#     print(x)
#     x = x + 1
# print('Acabou! ')

# while x < 10:
#     if x == 3:
#         x = x + 1
#         break # finaliza a execução do laço se a condição for True
#     print(x)
#     x = x + 1
# print('Acabou! ')

x = 0 # coluna
y = 0 # linha

# while x < 10:
#     y = 0
#     while y < 5:
#         print(f' {x} , {y}')
#         y += 1
#     x += 1 # x = x + 1
# print('Acabou! ')
while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [s]im ou [n]ão: ')

    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
         print('Você precisa digitar um número. ')
         continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - / *
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador inválido.')