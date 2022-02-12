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

print(f'\t\t\t--Produtos--')
soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos / len(produtos))

print(f'\t\t\t--Pessoas--')
soma_idades = reduce(lambda ac, p: p['idade'] + ac, pessoas, 0)
print(soma_idades / len(pessoas))
