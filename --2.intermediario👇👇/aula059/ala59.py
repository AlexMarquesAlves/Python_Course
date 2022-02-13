def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError as error:
        pass


numero = converte_numero(input('Digite um número: '))
print(numero + 5)
