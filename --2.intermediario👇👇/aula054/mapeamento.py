from dados import produtos, pessoas, lista

print('----> Mapeamento de lista com map() e list comprehension')
# nova_lista = map(lambda x: x*2, lista)
nova_lista = [x * 2 for x in lista]
print(lista)
print(list(nova_lista))
print()
print('----> Mapeamento de dicionários')

for produto in produtos:
    print(produto)
