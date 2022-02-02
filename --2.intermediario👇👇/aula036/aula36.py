print('-'*20, 'Exemplo Função', '-'*20)


def funcao(arg, arg2):
    return arg * arg2


var =funcao(2, 2)
print(var)
print()
print('-'*20, 'Sorted by Item', '-'*20)
lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]


def func(item):
    return item[1]


# lista.sort(key=func)
lista.sort(key=func, reverse=True)
print(lista)

print()
print('-'*20, 'Expressões Lambda', '-'*20)

a = lambda x, y: x * y
print(a(2, 2))
print()
list = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

print('-'*20, 'Sorted by Item', '-'*20)

list.sort(key=lambda item: item[1])
print(list)
print()

print('-'*20, 'Sorted by Item Reverse', '-'*20)

list.sort(key=lambda item: item[1], reverse=True)
print(list)
print()

print('-'*20, 'Sorted by Product', '-'*20)

print(sorted(list, key=lambda i: i[0], reverse=True))
print(list)
