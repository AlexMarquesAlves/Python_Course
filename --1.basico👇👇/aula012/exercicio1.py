"""
Faça um programa que peça ao usuario para digitar um número inteiro,
informe se este numero é par ou ímpar. Caso o usuario não digite um número
inteiro, informe que não é um número inteiro.
"""

number = input('Digite um número Inteiro: ')
if number.isnumeric():
    number = int(number)
    if (number % 2) == 0:
        print(f'O número {number} é Par. ')
    else:
        print(f'O número {number} é ímpar. ')
else:
    print("...Por Favor Digite um número Válido. ")
