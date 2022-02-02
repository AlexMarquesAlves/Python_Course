print()
"""
Funções - def em Python - *args **kwargs - (Parte 3)
"""


def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1, a2, a3, a4, a5, nome, a6)
    return nome, a6


var = func(1, 2, 3, 4, 5, nome='Luiz', a6='5')
print(var)
print()
print('-' * 15, '*Args', '-' * 15)


def func(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))


lista = [1, 2, 3, 4, 5]
n1, n2, *n = lista
print(n1, n2, n)
print()
print(*lista, sep='-')
print()
func(1, 2, 3, 4, 5)
print()
print('<- Tuple to list ->')
print()


def func(*args):
    args = list(args)
    args[0] = 20
    print(args)


func(1, 2, 3, 4, 5)
print()


def func(*args):
    for v in args:
        print(v)


func(1, 2, 3, 4, 5)
print()


def func(*args):
    print(args)


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2)
print()
print('-' * 13, '*Kwargs', '-' * 13)
print()


def func(*args, **kwargs):
    print(args)
    print(kwargs['nome'], kwargs['sobrenome'])


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Luiz', sobrenome='Miranda')

print()


def func(*args, **kwargs):
    print(args)

    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    else:
        print('Idade não existe')


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Luiz', sobrenome='Miranda', idade=30)

print()


def func(*args, **kwargs):
    print(args)

    idade = kwargs['idade']
    print(idade)


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Luiz', sobrenome='Miranda', idade=20)
