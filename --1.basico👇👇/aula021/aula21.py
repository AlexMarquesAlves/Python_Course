"""
Split, join, Enumerate em Python
* Split - Dividir um string # str
* Join - Juntar uma lista # str
* Enumerate - enumerar elementos da lista # list / iteráveis
"""
Split = "Split"
Join = "Join"
Enumarate = "Enumerate"
div = ''

string = "O Brasil é o o o país do futebol, o Brasil é penta."
lista_1 = string.split(' ')
lista_2 = string.split(',')

print('-----lista-1--------------------------------------------')
palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é "{palavra}" ({contagem}x)')

print('-----lista-2--------------------------------------------')

palavra = ''
contagem = 0
for valor in lista_2:
    qtd_vezes = lista_2.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é "{palavra}" ({contagem}x)')

print(f'{Split:-^100}')

string = "O Brasil é o o o país do futebol, o Brasil é penta."
lista_1 = string.split(' ')
lista_2 = string.split(',')

for valor in lista_2:
    print(valor.strip().capitalize())

print(f'{Join:-^100}')

string = 'O Brasil é penta.'
lista = string.split(' ')
string2 = ','.join(lista)

print(string)
print(lista)
print(string2)

print(f'{Enumarate:-^100}')
# string = 'O Brasil é penta.'
# lista = string.split(' ')
#
# for indice, valor in enumerate(lista):
#     print(indice, valor, lista[indice])

lista = [
    [1,2],
    [3,4],
    [5,6],
]

for v in lista:
    print(v[0], v[1])

print(f'{div:-^100}')

lista = [
    [0,'Luiz'],
    [1,'João'],
    [2,'Maria'],
]

for indice, valor in lista:
    print(indice, valor)

print(f'{div:-^100}')

lista = ['Luiz', 'João', 'Maria']

for indice, nome in enumerate(lista):
    print(indice, nome)

print(f'--------------------------------------Desenpacotamento-----------------------------------------------')

lista = ['Luiz', 'João', 'Maria']

n1, n2, n3 = lista

print(n2)
