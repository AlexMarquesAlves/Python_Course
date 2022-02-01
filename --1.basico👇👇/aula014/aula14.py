"""
Manipulando strings - Aula 6
    string indice
    fatiamento de strings [inicio:fim:passo]
    funções built-in len, abs, type, print, etc...
essas funcoes podem ser usadas diretamente em cada tipo

voce pode conferir tudo isso em:
https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/library/functions.html
"""
# positivos  [012345678]
texto      = 'Python s2'
# negativos  [987654321]

url = 'www.google.com.br/'

print(texto[2])
print(texto[8])
print(texto[6])

print(url[:-1])

nova_string = texto[2:6]
print(nova_string)

nova_string = texto[:6]
print(nova_string)

nova_string = texto[-1]
print(nova_string)

nova_string = texto[-9]
print(nova_string)

nova_string = texto[-9:-3]
print(nova_string)

nova_string = texto[:-1]
print(nova_string)

# passo
nova_string = texto[0:6:2]
print(nova_string)

nova_string = texto[0::3]
print(nova_string)

print(len(texto))
for letra in texto:
    print(letra)
