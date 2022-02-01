"""
Formatando Valores com modificadores — aula 13
:s -- Texto (string)
:d --Inteiros (int)
:f -- Números de ponto flutuante (float)
:.(NUMERO)f -- Quantidade de casas
:(CARACTERE)(> ou <, ou ^)(QUANTIDADE)(TIPO -s, d, ou f)

> -- Esquerda
< -- Direita
^ -- Centro
"""
num_1 = 10
num_2 = 3
divisao = num_1 / num_2

# :.()f
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

# :s
name = 'Luiz Otávio'
print(f'{name:s}')

# (caractere)
num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0<10}')

num_3 = 5515
print(f'{num_3:0^10}')

num_4 = 132
print(f'{num_4:0<10}')

# outros exemplos

nome = 'Otavio'
sobrenome = 'Miranda'

nome_formatado1 = '{:@<50}'.format(nome)
nome_formatado2 = '{n}{n}{n}{n}'.format(n=nome)
nome_formatado3 = '{n:0<20}'.format(n=nome)
nome_formatado4 = '{0:$^50} {1:#^50}'.format(nome, sobrenome)

print(nome_formatado1)
print(nome_formatado2)
print(nome_formatado3)
print(nome_formatado4)

print((50-len(nome))/2)
print(f'{nome:#^50}')

#
print(name.lower())
print(name.upper())
print(name.title())

