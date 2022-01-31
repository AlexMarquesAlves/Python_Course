"""
Faça um programa que peça ao usuario para digitar um número inteiro,
informe se este numero é par ou ímpar. Caso o usuario não digite um número
inteiro, informe que não é um número inteiro.
"""

number = input('Digite um número Inteiro: ')
if number.isnumeric():
    number = int(number)
    if (number % 2) == 0:
        print('Seu número é Par. ')
    else:
        print('Seu número é ímpar. ')
else:
    print("...Por Favor Digite um número Válido. ")
