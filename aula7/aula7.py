nome = 'Leonardo Marques'
idade = 22
altura = 1.85
e_maior = idade > 18
peso = 70
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos e seu imc é {:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos e seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))
