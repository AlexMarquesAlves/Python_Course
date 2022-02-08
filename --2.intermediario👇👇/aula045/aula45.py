lista = [0, 1, 2, 3, 4, 5]

print(f'\t\t', '----', 'Iteradores', '----')
print(hasattr(lista, '__iter__'))

# for v in lista:
#     print(v)
print(hasattr(lista, '__next__'))
lista = iter(lista)
print(hasattr(lista, '__next__'))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

print(f'\t\t', '----', 'Exemplo', '----')
import sys

lista = list(range(1000))
print(f'lista size: {sys.getsizeof(lista)} Bytes')

print(f'\t\t', '----', 'Geradores', '----')
import time


def gera():
    for n in range(100):
        yield n
        time.sleep(.1)


g = gera()
print(hasattr(g, '__iter__'))
print(hasattr(g, '__next__'))
# for v in g:
#     print(v)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(f'\t\t', '----', 'Exemplo', '----')


def gerar():
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor 3'
    yield variavel


g = gerar()
# print(next(g))
# print(next(g))
# print(next(g))
for v in g:
    print(v)

print(f'\t\t', '----', 'Exemplo 2', '----')

l1 = [x for x in range(1000)]
l2 = (x for x in range(1000))

print(f'l1 size: {sys.getsizeof(l1)} Bytes', type(l1))
print(f'l2 size: {sys.getsizeof(l2)} Bytes', type(l2))
