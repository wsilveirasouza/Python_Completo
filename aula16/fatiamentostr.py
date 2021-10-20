'''
Manipulando strings
* string indices
* fatiamento de strings
* funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo
'''
# Forma de acesso aos indices
# positivos [012345678]
texto     = 'Python s2'
# negativos-[987654321]

# acessando indice positivo
print(texto[2])

# acessando indice negativo
print(texto[:-8])

# fatiamento de string
nova_str = texto[-9:-6]
print(nova_str)
# indice de inicio - fim e passo 2
nova_str2 = texto[0:6:2]
print(nova_str2)
# função Len, conta caracteres
print(len(texto))

for letra in texto:
    print(letra)
