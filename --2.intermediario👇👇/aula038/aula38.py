print('-'*10, 'Dicionários em Python', '-'*10)
print('-'*10, 'Exemplo_1', '-'*10)

d1 = {'chave1': 'valor da chave'}
d1['nova_chave'] = 'Valor  da nova chave'  # adicinando novos valores ao dicionário

print(d1)
print(d1['chave1'])  # exibe apenas o valor..

print('-'*10, 'Exemplo_2', '-'*10)
d1 = dict(chave1='valor da chave', chave2='valor da outra chave')  # outra maneira de criar dicionários em Python
d1['nova_chave'] = 'Valor  da nova chave'

print(d1)
print('-'*10, 'Exemplo_3', '-'*10)

d1 = {'chave': 'valor', 'chave': 'valor', 'chave': 'valor real da chave', }  # Chaves precisam ter valor único
d1 = {1: 'valor', 2: 'valor', 3: 'valor real da chave', }
# d1['nova_chave'] = 'Valor  da nova chave'

print(d1)
print(d1[3])
print('-'*10, 'Exemplo_4', '-'*10)

di={ # Valores aceitos como chave para dicionários, precisam ser imutáveis
    'str': 'valor',
    123: 'Outro valor',
    (1,2,3): 'Tupla',
}

di['naoexiste'] = 'Agora existe.'
if 'naoexiste' in di:
    print(di['naoexiste'])

print('Oi')
print('-'*10, 'Exemplo_5', '-'*10)

di2={
    'str': 'valor',
    123: 'Outro valor',
    (1,2,3): 'Tupla',
}

di2['nomeQueEuQuero'] = 'Agora ela existe'

if di2.get('nomeQueEuQuero') is not None:  # outra maneira de verificação
    print(di2.get('nomeQueEuQuero'))

print(123)
print('-'*10, 'Exemplo_6', '-'*10)

di2={
    'str': 'valor',
    123: 'Outro valor',
    (1,2,3): 'Tupla',
}
# se já existir a chave, seu valor é atualizado

di2['str'] = 'Agora ela existe'

if di2.get('str') is not None:
    print(di2.get('str'))

print(123)
print('-'*10, 'Exemplo_7', '-'*10)

di3={
    'str': 'valor',
    123: 'Outro valor',
    (1,2,3): 'Tupla',
}
# Outra maneira de atualizar chaves -  usado update

di3.update({'novaChave':'Novo Valor'})  # update recebe um dicionário contendo um par de chave e valor

if di3.get('novaChave') is not None:
    print(di3.get('novaChave'))

print(123)
print('-'*10, 'Exemplo_8', '-'*10)

di4={
    'str': 'valor',
    123: 'Outro valor',
    (1,2,3): 'Tupla',
}

print('str' in di4)  # retorna o mesmo que o da linha abaixo
print('str' in di4.keys())  # retorna o mesmo que o da linha acima
print('valor' in di4.values())  # checando valores da chave

# Apagando chave 'str'
del di4['str']

print(di4)

print('-'*10, 'Exemplo_9', '-'*10)

di4={
    'str': 'valor',
    123: 'Outro valor',
    (1,2,3): 'Tupla',
}

print(len(di4))  # Verificação de quantos pares de chaves há em um dicionário

print('-'*10, 'Exemplo_10', '-'*10)

di4={
    'chave1': 'valor',
    'chave2': 'Outro valor',
    'chave3': 'Tupla',
}
# Iterando sobre o dicionário - Chaves -
print('-'*5, 'Chaves do Dicionário', '-'*5)
for k in di4:
    print(f'-> {k}')
print('-'*4, 'Valores do Dicionário', '-'*4)
# Iterando sobre o dicionário - Valores -
for v in di4.values():
    print(f'->> {v}')
print('-'*4, 'Items do Dicionário', '-'*4)
# Iterando sobre o dicionário - Items -
for k in di4.items():
    print(f'-> {k}')
print()  # Chave e valor separados
for k in di4.items():
    print(k[0], k[1])

print()  # Chave e valor Desempacotado
for k, v in di4.items():
    print(k, v)

print('-'*10, 'Exemplo_11', '-'*10)

clientes = {
    'cliente1': {
        'Nome': 'Luiz',
        'Sobrenome': 'Otávio',
    },
    'cliente2': {
        'Nome': 'João',
        'Sobrenome': 'Moreira',
    },
    'cliente3': {
        'Nome': 'Maria',
        'Sobrenome': 'Moreira',
    },
}
print()
#  Iterando sobre dicionário dentro do dicionário
for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

print('-'*10, 'Exemplo_12', '-'*10)

d4 = { 1: 'a', 2: 'b', 3: 'c'}
v = d4  # isso não cria um novo dicionário
v[1] = 'Luiz'

print(d4)
print(v)
print(d4 == v)
print()
print(f"\t\t| Shell copy |")
d5 = { 1: 'a', 2: 'b', 3: 'c'}
v5 = d5.copy()
v5[1] = 'Luiz'

print(d5)
print(v5)
print()
print(f"\t\t| Shell copy |")
d6 = { 1: 'a', 2: 'b', 3: 'c', 'd':['Luiz', 'Otávio']}
v6 = d6.copy()

v6[1] = 'Luiz'
v6['d'][0] = 'Joãozinho'  # altera o valor nas duas listas

print(d6)  # o valor também é alterado na shell copy
print(v6)

print()
import copy
print(f"\t\t| Deep Copy |")
d7 = { 1: 'a', 2: 'b', 3: 'c', 'd':['Luiz', 'Otávio']}
v7 = copy.deepcopy(d7)  # com isso não se altera valores no dicionário original

v7[1] = 'Luiz'
v7['d'][0] = 'Joãozinho'

print(d7)  # o valor agora não é alterado
print(v7)

print()

d8 = { 1: 'a', 2: 'b', 3: 'c', 'd':('Luiz', 'Otávio')}
v8 = d8.copy()

v8[1] = 'Luiz'
v8['d'] = ('Otávio', 'Luiz')
print(f"\t\t| Tuplas |")
print(d8)
print(v8)
print('-'*10, 'Exemplo_13', '-'*10)
print(f"Convertendo lista em dicionário")
# É possivel converter em dicinário pois há pares
lista = [  # Também possivel com Tuplas
    ['c1', 1], # ('c1', 1),
    ['c2', 2], # ('c2', 2),
    ['c3', 3], # ('c3', 3),
]

print()

dicio = dict(lista)
print(f'\t{dicio}')
print(f'\t',dicio['c3'])

print('-'*10, 'Exemplo_14', '-'*10)
print(f"\t| .pop | .popitem |")
dicio = {
    1: 2,
    2: 3,
    4: 5,
}

dicio.pop(4)  # ou .popitem()
print(dicio)


print(f"\t| Concatenando |")
dicio1 = {
    1: 2,
    2: 3,
    4: 5,
}

dicio2 = {
    'a': 'b',
    'c': 'd',
}

dicio1.update(dicio2)
print(dicio1)

