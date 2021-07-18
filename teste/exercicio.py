"""
Criando um visualizador de tabuadas
Você escolhe a tabuada que deseja visualizar
Utilizando a estrutuda de controle for e método de entrada com cast.
"""

c = 0
tabuada = 0
resultado = 0

tabuada = int(input('Digite a tabuada de sua preferência: '))

resultado = 0

for c in range(0, 10):
    resultado += tabuada    
    print(resultado)
