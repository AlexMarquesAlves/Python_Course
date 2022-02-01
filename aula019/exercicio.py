secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break

    letra = input('Digite um letra: ').lower()

    if len(letra) > 1 or letra.isnumeric():
        print('😒 isso não vale, digite apenas uma letra, números também não são permitidos')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Show!!, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'Affff: a letra "{letra}" NÃO EXISTE na palavra secreta')
        digitadas.pop()

    secreto_temp = ''
    for letra_secreta in secreto:
       if letra_secreta in digitadas:
           secreto_temp += letra_secreta
       else:
            secreto_temp += '*'

    # print(secreto_temp)
    if secreto_temp == secreto:
        print(f'Que legal! VOCÊ GANHOU!!! A palavra era {secreto.title()}.')
        break
    else:
        print(f'A palavra secreta está assim: "{secreto_temp}"')

    if letra not in secreto:
        chances -= 1
        continue

    print(f'Você ainda tem {chances} tentativas.')
    print()

