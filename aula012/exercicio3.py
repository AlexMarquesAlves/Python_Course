"""
Faça um programa que peça o primeiro nome do usuario. se o nome tiver 4 letra ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

usuario = input('Digite seu primeiro nome: ')
qtd_caracteres = len(usuario)

short = qtd_caracteres <= 4
normal = 5 <= qtd_caracteres <= 6
large = qtd_caracteres >= 7

if short:
    print(f'{qtd_caracteres} caracteres, Seu nome é curto')
elif normal:
    print(f'{qtd_caracteres} caracteres, Seu nome é normal')
elif large:
    print(f'{qtd_caracteres} caracteres, Seu nome é muito grande')
else:
    print('Error')
