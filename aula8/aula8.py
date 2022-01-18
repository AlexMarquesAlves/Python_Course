"""
* Criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar variáveis com o ano atua (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casa decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-strings (com as chaves)
"""

nome = 'Leonardo'
idade = 22
altura = 1.80
peso = 70
data_atual = 2022
ano_nascimento = data_atual - idade
IMC = peso / altura ** 2


print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {IMC:.2f}.')
print(f'{nome} nasceu em {ano_nascimento}.')

