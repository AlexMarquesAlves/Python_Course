print(f'--Alterando valores entre variáveis--')
print()
print(f'Forma comum', '-'*25)
x = 10
y = 'Luiz'

z = x
x = y
y = z

print(f'X={x} e Y= {y}')
print()
print(f'Forma em Python', '-'*21)

x = 10
y = 'Luiz'
x, y = y, x

print(f'X={x} e Y= {y}')

print()
print(f'Exemplo', '-'*28)

x = 10
y = 'Luiz'
z = 'Otávio'
x, y, z = z, x, y

print(f'X={x} e Y= {y} e Z={z}')
