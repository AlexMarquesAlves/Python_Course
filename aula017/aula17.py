#       Índices
#       0123456789........................33
frase = 'a rato roeu a roupa do rei de roma'  # Iterável
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_do_usuario = input('Qual letra desejas por em Maiúsculo? ')

# Iteração <- Iterar
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += 1
    contador += 1

print(nova_string)
