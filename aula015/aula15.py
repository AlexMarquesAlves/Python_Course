"""
While em python
utilizado para realizar acoes enquanto uma condicao for verdadeira

Requerido: entender condicoes e operadores
"""

"""
while True:
    nome = input('Qual seu nome? ')
    print(f'óla {nome}')

print('não será executado')
"""
x = 0
while x < 100:
    if x == 3:
        x = x + 1
        continue

    print(x)
    x = x + 1

print('Acabou! ')

# exemplo 2

x = 0  # coluna
while x < 10:
    y = 0  # linha

    while y < 5:
        print(f'({x},{y})')
        y += 1

    x += 1

print('Acabou! ')
