from dados import produtos, pessoas, lista

print('----> Filtrando os dados da lista com List Comprehension')
# nova_lista = filter(lambda x: x > 5, lista)
nova_lista = [x for x in lista if x > 5]
print(list(nova_lista))
print('----> Filter >> Produtos')


def filtra(produto):
    if produto['preco'] > 50:
        produto['e_caro'] = True
    return True



nova_lista = filter(filtra, produtos)

for produto in nova_lista:
    print(produto)
