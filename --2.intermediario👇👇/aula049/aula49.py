"""
Considerando duas listas de inteiros ou floats (lista A e Lista B)
some os valores nas listas retornando uma nova lista com valores somados:

se uma lista for maior que a outra, a soma só vai considerar o tamanho da menos

exemplo:
lista_a  = [1, 2, 3, 4, 5, 6, 7]
lista_b  = [1, 2, 3, 4]

============ resultado
lista_soma = [2, 4, 6, 8]
"""
print(f'\t\t\tMinha Solução')
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
listas = zip(lista_a, lista_b)
lista_soma = []
for v in listas:
    lista_soma.append(sum(v))

print(f'--> {lista_soma}')

