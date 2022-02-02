print("-" * 12, "Exercício_1", "-" * 12)
"""
1 - Crie uma função que exiba uma saudação com os parameters saudação e 
nome.
"""


def saudacao(sudacao, nome):
    print(sudacao, nome)


nome = input('Qual vosso nome? ')
print()
boas_vindas = saudacao('Bem-Vindo!', nome)

print("-" * 8, "Resultado no curso", "-" * 8)


def saudacao(sudacao, nome):
    print(f'{sudacao} {nome}')


saudacao('Olá', 'Joãozinho')
saudacao('Oi', 'Maria')
saudacao('Hey', 'Eduardo')
