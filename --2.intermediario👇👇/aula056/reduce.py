from dados import produtos, pessoas, lista
from functools import reduce
print('----> Exemplo de Acumulador')
acumula = 0
for item in lista:
    acumula += item

print(acumula)

print('----> Exemplo de Reducer')
print(f'\t\t\t--Lista--')
soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)
