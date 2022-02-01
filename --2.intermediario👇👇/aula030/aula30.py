print()
"""
Funções - def em python (Parte 1)
"""


def saudacao(msg='Olá', nome='usuario'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    # print(msg, nome)
    return f'{msg} {nome}'


saudacao(nome='Zezinho', msg='Hi')
saudacao('Oi', 'Luiz')
saudacao('Hello', 'Maria')
saudacao('Olá', 'Otávio')
saudacao('Olá', 'Joao')

variavel = saudacao()

print(variavel)
