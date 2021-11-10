'''
USANDO O VALOR DE UMA FUNCAO EM OUTRA
'''
variavel = 'Wellington Silveira de Souza'
def func():
    outra_variavel = 'Wellington Souza'
    return outra_variavel

def func2(arg):
    print(arg)
    
var = func()
func2(var)

print(variavel)