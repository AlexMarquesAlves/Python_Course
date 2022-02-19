import os

try:
    file = open('abc.txt', 'w+')
    file.write('Linha')
    file.seek(0)
    print(file.read())
finally:
    file.close()

print('########################')

with open('abc.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0)
    print(file.read())

print('Somente leitura')
with open('abc.txt', 'r') as file:
    print(file.read())

print('Append mode')
with open('abc.txt', 'a+') as file:
    file.write('Outra Linha\n')
    file.write('Outra Linha\n')
    file.write('Outra Linha\n')

    file.seek(0)
    print(file.read())

os.remove('abc.txt')
