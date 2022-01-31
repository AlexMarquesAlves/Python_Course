"""
Faça um programa que pergunte a hora ao usuario e, baseando-se no horario
descrito, exiba a saudação apropriada. Ex.
Bom Dia 0-11, Boa Tarde 12-18 e Boa Noite 19-23.
"""

nowTime = input('Que horas são agora em número inteiro? ')

if nowTime.isnumeric():
    nowTime = int(nowTime)
    dia = 0 <= nowTime <= 11
    tarde = 12 <= nowTime <= 18
    noite = 19 <= nowTime <= 23

    if dia:
        print('Bom Dia! ')
    elif tarde:
        print('Boa Tarde! ')
    elif noite:
        print('Boa Noite! ')
else:
    print('Digite um número inteiro ')
