"""
Documentação e funções built-in úteis

# isnumeric, isdigit, isdecimal
# números e positivos
print(num_1.isnumeric())
print(num_2.isnumeric())
"""

num_1 = input('Digite um número: ')
num_2 = input('Digite outro número: ')

try:
    num_1 = float(num_1)
    num_2 = float(num_2)

    print(num_1 + num_2)
except:
    print('Não pude converter os números para realizar contas.')
