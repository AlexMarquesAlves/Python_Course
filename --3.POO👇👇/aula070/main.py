from pessoa import Pessoa

# p1 = Pessoa()
# p2 = Pessoa()
#
# print()
# print(f'P1 é != de P2')
# print(p1)
# print(p2)
# print()
# # Atributo nome na classe
# p1.nome = 'Luiz'
# p2.nome = 'João'
# print(p2.nome)


# Atribuindo direto na classe
print(f'-' * 20)
p1 = Pessoa('Luiz', 29)
p2 = Pessoa('João', 32)
p1.comer('Maça')
p1.parar_comer()
# Ponendo persona a hablar
p1.falar('POO')
p1.parar_falar()

print(f'-'*20)
# Metodos independentes
p1.falar('POO')
p2.falar('Filmes ')
p1.comer('Churrasco')
print(f'-'*20)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())


# p2 = Pessoa(f'João, {32}')
