print()
"""
Funções - def em Python - return - (Parte 2)
"""


def funcao(variable):
    return variable


variavel = funcao('valor que eu quero')

# if variavel:
#     print(variavel)
# else:
#     print('Nenhum valor. ')

print()
print('-' * 9, 'Exemplo de Função', '-' * 9)
print()


def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2


divide = divisao(8, 2)
if divide:
    print(divide)
else:
    print('Conta inválida')

print()
print('-' * 9, 'Exemplo de Função', '-' * 9)
print()


def dumb():
    return [1, 2, 3, 4, 5]


var = dumb()
print(var, type(var))


print()
print('-' * 9, 'Exemplo de Função', '-' * 9)
print()


def f(var):
    print(var)


def dumb():
    return f


var = dumb()
print(id(var), id(f))

if var == f:
    print('Var é igual a f')
else:
    print('Blaaaaaaaaaaaa')

var('Pode imprimir algo na tela.')

print()
print('-' * 9, 'Exemplo de Função', '-' * 9)
print()


def dumb():
    return ('Luiz', 'Otávio')


var = dumb()
print(var, type(var))
print(var[0], type(var))
print(var[1], type(var))
