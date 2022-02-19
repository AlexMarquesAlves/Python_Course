# Funções como variáveis
def fala_oi():
    print('Oi')


# A variável é igual a função
variavel = fala_oi
print(type(variavel))  # function
variavel()  # Oi


# Uma função dentro de outra
def master():
    # Função interna
    def slave():
        print('Oi')

    # Função a ser executada
    return slave


# Variável recebe função
variavel = master()
# Executa a função interna de master
variavel()


# Função como parâmetro
def master(funcao):
    # Função interna
    def slave():
        # executa a função enviada
        funcao()

    # Retorna a função interna sem executar
    return slave


# Uma função qualquer
def fala_oi():
    print('Oi')


# Variável como função
variavel = master(fala_oi)
# Executa a variável/função
variavel()


# Recebe uma função
def master(funcao):
    # Cria uma função interna
    def slave():
        # Decora
        print('Estou decorada.')
        # Executa a função enviada
        funcao()

    # Retorna a função interna sem executar
    return slave


# Uma função qualquer
def fala_oi():
    print('Oi')


# Decorando
fala_oi = master(fala_oi)
fala_oi()
