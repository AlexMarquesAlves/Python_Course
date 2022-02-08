# listas, tuples, str, --> sequences -> iterável 
nome = 'Luiz Otávio'
iterador = iter(nome)
gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print()

for letra in gerador:
    print(letra)
try:
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))

except:
    pass

print('Cadê os Valores? ')
for valor in iterador:
    print(valor)

# for letra in nome:
#     print(letra)
#
# print('#' * 80)
#
# for letra in nome:
#     print(letra)
