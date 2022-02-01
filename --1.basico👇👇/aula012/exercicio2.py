"""
Faça um programa que pergunte a hora ao usuario e, baseando-se no horario
descrito, exiba a saudação apropriada. Ex.
Bom Dia 0-11, Boa Tarde 12-18 e Boa Noite 19-23.
"""

nowTime = input('Que horas são agora?(0-23) ')

if nowTime.isnumeric():
    nowTime = int(nowTime)
    dia = 0 <= nowTime <= 11
    tarde = 12 <= nowTime <= 18
    noite = 19 <= nowTime <= 23

    if dia:

        print(f'São {nowTime}h, Bom Dia! ')
    elif tarde:
        print(f'São {nowTime}h, Boa Tarde! ')
    elif noite:
        print(f'São {nowTime}h, Boa Noite! ')
else:
    print('Digite um número inteiro ')
