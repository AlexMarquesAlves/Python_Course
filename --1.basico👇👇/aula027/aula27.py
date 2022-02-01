"""
for / while
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""
line = 'Desafio Contador'
me = 'Feito por mim'
by_class = 'Resultado da aula'
print(f'{line:-^35}')

print()

print(f'{me:-^35}')
crescente = -1
decrescente = 11

while crescente < 10:
    if decrescente <= 11:
        decrescente -= 1
    crescente += 1
    if crescente >= 9:
        break
    print(crescente, decrescente)

print()
print(f'{by_class:-^35}')

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)



