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
