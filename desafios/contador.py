'''
Desafio de contadores: 
FOR / WHILE
Criar 2 contadores simultâneos
sendo que um irá contador progressivamente 
enquanto o outro regressivamente
* 0 a 8 - 10 a 2
'''
contP = 0
contR = 10

while contP <= 8:
    print(contP, contR)
    contP = contP + 1
    contR = contR - 1

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)
