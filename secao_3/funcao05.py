'''
FUNÇÕES (DEF) EM PYTHON - *args **kwargs
Aula 16 (parte 3)
'''
# Tuplas - não podem ser alteradas
def funcPrimeira(*args): # (args) empacotamento e desempacotamento
    print(args)
# desempacotando lista
lista = [1,2,3,4,5]
n1, n2, *n = lista
print(n1,n2, n)
print(*lista, sep='-') # desempacotando

def funcSegunda(*args):
    print(args)
funcSegunda(1,2,3,4,5)
# funcao sem saber a quantidade de argumentos
def func(*args):
    print(args)

lista = [1,2,3,4,5]
print(lista)
print(*lista)

def funcArg(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))

funcArg(1,2,3,4,5)

def funcFor(*args):
    for v in args:
        print(v)

funcFor(1, 2, 3, 4, 5)

def funcListas(*args):
    print(args)

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
funcListas(*lista, *lista2)

# Argumentos com palavras chaves
def funcLista(*args, **kwargs):
    print(args)

    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)
    else:
        print('Idade não existe!')

lista3 = [1,2,3,4,5]
lista4 = [10,20,30,40,50]
funcLista(*lista3, *lista4, nome='wellington', sobrenome='souza', idade='39')
