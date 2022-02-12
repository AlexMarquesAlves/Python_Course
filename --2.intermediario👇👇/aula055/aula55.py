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

print('----> Filter >> Pessoas')


def menor(pessoa):
    if pessoa['idade'] < 18:
        return True


def maior(pessoa):
    if pessoa['idade'] >= 18:
        return True


menor_de_idade = filter(menor, pessoas)
maior_de_idade = filter(maior, pessoas)

print(f'\t\tMenor de idade')
for pessoas in menor_de_idade:
    print(pessoas)
print()
print(f'\t\tMaior de idade')
for pessoas in maior_de_idade:
    print(pessoas)
