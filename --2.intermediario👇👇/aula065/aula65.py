# Funções como variáveis
def fala_oi():
    print('Oi')


# A variável é igual a função
variavel = fala_oi
print(type(variavel))  # function
variavel()  # Oi