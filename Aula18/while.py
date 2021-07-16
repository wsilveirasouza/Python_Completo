# Índices
# 01234567890000000000000000000000033
# Strings tem indices, esses indices são iteraveis
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

# while contador < 10:
#     print(frase[contador], contador)
#     contador += 1

# while contador < tamanho_frase:
#     # print(frase[contador], contador)
#     nova_string += frase[contador]
#     contador += 1

#     print(nova_string)

# while contador < tamanho_frase:
#     letra = frase[contador]
#     if letra == 'r':
#         nova_string += 'R'
#     else:
#         nova_string += letra
#     contador += 1

#     print(nova_string)

input_do_usuario = input('Qual letra deseja colocar maiuscula: ')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1

    print(nova_string)