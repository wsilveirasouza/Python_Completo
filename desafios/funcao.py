'''
Exercícios propostos
'''
'''
1. Crie uma função que exibe uma saudação com os parâmetros 'saudacao' e 'nome'.
'''
# def ola(saudacao, nome):
#     print(f'{saudacao} {nome}')
#
# ola('Bom dia', 'Wellington')

'''
2. Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.
'''
def soma(a, b, c):
    print(a+b+c)

soma(8,9,15)

'''
3 . Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex. 10%).
Retorne (return) o valor do primeiro número somado do aumento do percentual do mesmo.
'''
def aumento_percentual(valor, percentual):
    return(valor + (valor * percentual / 100))

montante = aumento_percentual(50,10)

print('O resultado é: ',montante)

'''
4. FizzBuzz - Se o parâmetro da função for divisível por 3, retorne fizz, se o parâmetro da função for divisível por 5
retorne buzz. Se o parâmetro da função for divisível por 3 e 5 retorne FizzBuzz, caso contrário, retorne o número enviado.
'''
def fizzbuzz(a):

    if a % 3 == 0 and a % 5 == 0:
        return f'FizzBuzz, este valor é divisivel por 3 e 5.'
    if a % 3 == 0:
        return f'Fizz, este valor é divisivel por 3.'
    if a % 5 == 0:
        return f'Buzz, este valor é divisivel por 5.'
    return(a)

resultado = fizzbuzz(int(input('Insira um valor: ')))

print(resultado)
