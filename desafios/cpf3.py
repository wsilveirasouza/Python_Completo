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
while True:
    # cpf = '16899535009'
    cpf = input('Digite um cpf: ')
    novo_cpf = cpf[:-2]

    cont_reverso = 10

    total = 0

    for index in range(19):
        if index > 8:
            index -= 9

        total += int(novo_cpf[index]) * cont_reverso

        # print(cpf[index],index, cont_reverso) 

        cont_reverso -= 1
        if cont_reverso < 2:
            cont_reverso = 11
            digito = 11 - (total % 11)

            if digito > 9:
                digito = 0
            total = 0
            novo_cpf += str(digito)

    # print(novo_cpf)
    
    if cpf == novo_cpf:
        print('CPF Válido')
    else:
        print('CPF Inválido')
