print()
'''
Combinations, Permutations e Products - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produtos - Ordem importa e repete valores únicos
'''
from itertools import combinations, permutations, product

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabricio', 'Rosa', ]
print('----', 'Combinations', '----')

for grupo in combinations(pessoas, 3):
    print(grupo)

print()
print('----', 'Permutations', '----')

for grupo in permutations(pessoas, 2):
    print(grupo)

print()
print('----', 'Products', '----')

for grupo in product(pessoas, repeat=2):
    print(grupo)
