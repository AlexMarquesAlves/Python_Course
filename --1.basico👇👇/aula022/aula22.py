"""
* Enumerate - Enumerar elementos da lista # list
"""
div = ''

lista = [
    ['Edu', 'João', 'Luiz'],  # 0
    ['Maria', 'Aline', 'Joana'],  # 1
    ['Helena', 'Ed', 'Lu'],  # 2
]
# print(lista[1][2])

enumerada = list(enumerate(lista))
print(enumerada[1][1][2])

"""
[ <-- Enumerate

    (0, ['Edu', 'João', 'Luiz']),  # 0
    (1, ['Maria', 'Aline', 'Joana']),  # 1
    (2, ['Helena', 'Ed', 'Lu'])  # 2
]
"""
print()
print(f' Empacotado{div:-^35}')

for v1 in enumerate(lista, 53):
    print(v1, )
print()
print(f' Desempacotado{div:-^35}')

for v1 in enumerate(lista, 53):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(minha_lista)
    print(nome1, nome2, nome3)
    print()
