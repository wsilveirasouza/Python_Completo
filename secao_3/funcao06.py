'''
FUNÇÕES: PYTHON 3
parte 4
'''
# variavel global
variavel = 'valor'

def func():
    print(variavel)
# não é possível alterar uma variavel global de dentro do escopo de uma função
def func2():
    # ao menos que insira dentro da função o argumento 'global'
    # global variavel
    variavel = 'outro valor'
    print(variavel)

func()
func2()

print(variavel)

