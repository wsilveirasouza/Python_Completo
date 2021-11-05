'''
Exercícios propostos
'''
'''
1. Crie uma função que exibe uma saudação com os parâmetros 'saudacao' e 'nome'.
'''
def ola(saudacao, nome):
    print(saudacao,nome)

ola('Bom dia', 'Wellington')

'''
2. Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.
'''
def soma(a, b, c):
    return(a + b + c)

resultado = soma(8,9,14)

print('O resultado da operação é: ',resultado)

'''
3 . Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex. 10%).
Retorne (return) o valor do primeiro número somado do aumento do percentual do mesmo.
'''
def margem(a,b):
    return(a + (a * b/100))

montante = margem(50,10)

print('O resultado é: ',montante)

'''
4. FizzBuzz - Se o parâmetro da função for divisível por 3, retorne fizz, se o parâmetro da função for divisível por 5
retorne buzz. Se o parâmetro da função for divisível por 3 e 5 retorne FizzBuzz, caso contrário, retorne o número enviado.
'''
def fizzbuzz(a):
    if a % 3 == 0 and a % 5 == 0:
        print('FizzBuzz')
    elif a % 3 == 0:
        print('Fizz')
    elif a % 5 == 0:
        print('Buzz')
    else:
        print('O valor informado foi: ',a)

resultado = fizzbuzz(int(input('Insira um valor: ')))

print(resultado)
