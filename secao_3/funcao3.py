'''
FUNÇÃO
'''
def dumb():
    return [1,2,3,4,5]

var = dumb()
print(var, type(var))

def f(var):
    print(var)

def dumb2():
    return f

var = dumb2()
print(type(var))

print(id(var), id(f))

if var == f:
    print('var é igual a f.')
else:
    print('var é diferente de f.')
