"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
# booleanos = True
# inteiros = 10
# flutuante = -10.10
# strings = 'Textos'
#   +     0    1    2    3    4     5
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
#   -     6    5    4    3    2     1

print(lista[5])
print('----------------------------------------')
#
print(lista[0:3])
print('----------------------------------------')
#
print(lista[2:])
print('----------------------------------------')
#
print(lista[::2])
print('----------------------------------------')
#
print(lista[::-1])
print('----------------------------------------')
#
print('Listas----------------------------------------')
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2

print(l1)
print(l2)
print('Concatenado l1+l2----------------------------------------')
print(l3)
print('extend----------------------------------------')
l1.extend('a')

print(l1)
print('append----------------------------------------')
l2.append('b')

print(l2)
print('insert----------------------------------------')
l2 = [4, 5, 6]
l2.insert(0, 'banana')

print(l2)
print('pop----------------------------------------')
l2.pop()

print(l2)
print('nova-lista----------------------------------------')
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2.insert(0, 'banana')
print(l2)
print('del----------------------------------------')
del(l2[0])

print(l2)
print('max, min----------------------------------------')
print(max(l2))
print(min(l2))
print('range----------------------------------------')
l1 = list(range(0, 10))
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

soma = 0
for valor in l2:
    soma = soma + valor

print(soma)
print('----------------------------------------')
elemento = ['String',True, 10, -20.5]

for elem in elemento:
    print(f'O tipo do elemento é {type(elem)}, e seu valor é {elem}.')

