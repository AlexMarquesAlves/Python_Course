print()
"""
1 - Crie uma função que recebe uma função-2 como parâmetro e retorne o valor da
função-2 executada.
"""


def ola_mundo():
    return 'Olá Mundo! '


def master(msg):
    return msg()


executando = master(ola_mundo)
print(executando)
