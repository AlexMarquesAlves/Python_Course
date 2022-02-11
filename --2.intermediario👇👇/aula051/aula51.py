print()
from types import GeneratorType

variavel = zip('Alo', 'Alo')
print(next(variavel))
print(next(variavel))
print(next(variavel))

print(isinstance(variavel, GeneratorType))
variavel = ((x, y) for x, y in zip('Alo', 'Alo'))
print(isinstance(variavel, GeneratorType))
"""
Count - Itertools
"""
print('#'*30)
from itertools import count

contador = count(start=5, step=.1) # Causa um loop infinito quando usado num loop for

for valor in contador:
    print(round(valor,2))

    if valor >= 10:
        break

print('#'*30)
from itertools import count

contador = count(start=-1, step=-1) # Causa um loop infinito quando usado num loop for

for valor in contador:
    print(round(valor,2))

    if valor >= 10 or valor <=-10:
        break

print('#'*30)

contador = count()
lista = ['Luiz','João', 'Maria']
lista = zip(contador, lista)
print(list(lista))
