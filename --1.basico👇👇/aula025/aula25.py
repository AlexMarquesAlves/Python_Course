"""
Operação ternária em Python
"""
div = 'Operador ternário'
ex = 'Exemplo'
logged_user = False
print("----logged_user----", "False")

if logged_user:
    msg = 'Usuário logado'
else:
    msg = 'Usuário precisa logar'

print(msg)

print()
logged_user = True
print("----logged_user----", "True")

if logged_user:
    msg = 'Usuário logado'
else:
    msg = 'Usuário precisa logar'

print(msg)

print()
print(f'{div:-^35}')
print()
logged_user = True
msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar'

print(msg)
print()
print(f'{ex:-^35}')

idade = input('Qual vossa idade? ')
if not idade.isnumeric():
    print('Digite penas números.')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar'

print(msg)


