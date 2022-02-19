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
