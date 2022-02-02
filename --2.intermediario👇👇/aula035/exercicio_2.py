print('-' * 12, 'Exercise_2', '-' * 12)
"""
2 - Crie uma função-1 que recebe uma função-2 com parâmetro e retorne o valor da
função executada. faça a função-1 executar duas funções que recebam um número
diferente de argumentos.
"""


def master(func, *args, **kwargs):
    return func(*args, **kwargs)


def say_hello(name):
    return f'Hello {name}!'


def greeting(name, salutation):
    return f'{salutation}! {name}.'


running = master(say_hello, 'Leo')
running2 = master(greeting, 'Leo', salutation='Good Day')
print(running)
print(running2)
