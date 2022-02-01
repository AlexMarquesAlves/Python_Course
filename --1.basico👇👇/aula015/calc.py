# Simple Calc

while True:
    print()
    num_1 = input('Digite um número: ')
    operador = input('Digite um operador: ')
    num_2 = input('Digite outro número: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Voçê precisa digitar um número válido')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print('O resultado é...', num_1 + num_2)
    elif operador == '-':
        print('O resultado é...', num_1 - num_2)
    elif operador == '/':
        print('O resultado é...', num_1 / num_2)
    elif operador == '*':
        print('O resultado é...', num_1 * num_2)
    else:
        print('Operador Inválido')

    sair = input('Desejas Sair? [s]im ou [n]ão: ')

    if sair == 's':
        break
    else:
        continue
