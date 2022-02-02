print('-'*13,'Exemplo_1', '-'*13)
variavel = 'valor'


def func():
    print(variavel)


def func2():
    variavel = 'outro valor'
    print(variavel)


func()
func2()

print(variavel)


print()
print('-'*13,'Exemplo_2', '-'*13)
print('-'*4,'Alterando variaveis globais', '-'*4)

variavel = 'valor'


def func():
    print(variavel)


def func2():
    global variavel
    variavel = 'outro valor'
    print(variavel)


func()
func2()

print(variavel)

print()
print('-'*5,'Alterando pelo parametro', '-'*5)

variavel = 'valor'


def func():
    print(variavel)


def func2(arg=None):
    arg = arg.replace('v', 'c')
    return arg


func()
outra_variavel = func2(arg=variavel)

print(outra_variavel)

print()
print('-'*13,'Exemplo_3', '-'*13)

variavel = 'valor'


def func():
    # print(variavel)  # Essa linha gera um error - variavel definida depois de usada
    variavel = 1234
    print(variavel)



func()

print()
print('-'*13,'Exemplo_4', '-'*13)
print('-'*8,'Conectando funções', '-'*8)


def func():
    outra = 'Leonardo'
    return outra


def func2(arg):
    # print(outra)  # essa linha gera error - variavel não definida
    print(arg)

var = func()
func2(var)

