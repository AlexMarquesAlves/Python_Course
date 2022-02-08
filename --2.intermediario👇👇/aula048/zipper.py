print()
"""
Zip - Unindo Iteráveis
Zip_longest - Itertools
"""

# Código
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

print(f'\t\tExemplo de Zip')
print()

cidades_estados = zip(estados, cidades)
print(dict(cidades_estados))

# for valor in cidades_estados:
#     print(valor)
print('#'*30)

print()
print(f'\tExemplo de Zip_longest')
from itertools import zip_longest, count
print()

cidades_estados = zip_longest(estados, cidades, fillvalue='Estado')
print(list(cidades_estados))

print('#'*30)
print()
print(f'\t\t\tExemplo')
indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(indice, estados, cidades)

for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)

print('#'*30)
