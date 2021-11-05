'''
-------------------------------------------
Desafio: Validar CPF
CPF: 168.995.350-09
-------------------------------------------
1 * 10 = 10          # 1 * 11 = 11 <-
6 * 9  = 54          # 6 * 10 = 60
8 * 8  = 64          # 8 * 9  = 72
9 * 7  = 63          # 9 * 8  = 72
9 * 6  = 54          # 9 * 7  = 63
5 * 5  = 25          # 5 * 6  = 30
3 * 4  = 12          # 3 * 5  = 15
5 * 3  = 15          # 5 * 4  = 20
0 * 2  = 0           # 0 * 3  = 0
                     # 0 * 2  = 0
                     #
        297          #         343
11 - (297 % 11) = 11 #  11 - (343 % 11) = 9
11 > 9 = 0           #
Dígito 1 = 0         # Dígito 2 = 9

'''
cpf = '16899535009'
novo_cpf = cpf[:-2] # Elimina os dois últimos dígitos do CPF
reverso = 10 # Contador reverso
total = 0

for index in range(19):
    if index > 8: # Primeiro índice vai de 0 a 9,
        index -= 9 # São os 9 primeiros dígitos do CPF

    total += int(novo_cpf[index]) * reverso
    
    # print(cpf[index], index, reverso)
    
    reverso -= 1 # Decrementa o contador reverso
    if reverso < 2:
        reverso = 11
        digito = 11 - (total % 11)

        if digito > 9: # Se o dígito for > que '9' o valor é '0'
            digito = 0 
        total = 0 # Zera o total

        novo_cpf += str(digito) # Concatena o dígito gerado no novo CPF
# verificando como está o cpf
print(novo_cpf)
# Evita sequencias. Ex: 111111111111, 00000000000...
# sequencia = novo_cpf = str(novo_cpf[0]) * len(cpf)

# Sequencias avaliam como verdadeiro, checagem
if cpf == novo_cpf:
    print('Válido')
else:
    print('Inválido')