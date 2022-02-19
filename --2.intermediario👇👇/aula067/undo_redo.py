comandos_feitos = []
comandos_desfeitos = []
lista_tarefas = []


def adiciona():
    tarefa = input('Qual o nome da tarefa ? ')
    lista_tarefas.append(tarefa)
    comandos_feitos.append(tarefa)
    print(f"A tarefa: {tarefa}, foi adicionada com sucesso")


def lista():
    if not lista_tarefas:
        return print('A vossa lista está vazia')
    else:
        return print(lista_tarefas)


def apaga():
    if not lista_tarefas:
        return print('Não há tarefas para serem apagadas')
    else:
        removido = lista_tarefas.pop()
        comandos_desfeitos.append(removido)
        return print(f'Você removeu com sucesso a tarefa {removido}')


def desfazer():
    if not comandos_desfeitos:
        return print('Não há comandos para desfazer')
    else:
        refazer = comandos_desfeitos.pop()
        lista_tarefas.append(refazer)
        comandos_feitos.append(refazer)
        return print(f'Tu acabas de desfazer a ultima tarefa {refazer}')


def lista_tudo():
    if lista_tarefas == [] and comandos_feitos == [] and comandos_feitos == []:
        return print('Não há nada em vossas listas.')
    else:
        return print(
            f'Vossa lista de tarefas contém: {lista_tarefas}\n Sua lista de comandos feitos contém: {comandos_feitos} Sua lista de comandos desfeitos contém: {comandos_desfeitos}')


def menu():
    menu = True
    while menu:
        print(""""
        Escolha uma opção:\n
        1- Adicionar tarefa
        2- listar tarefa(s)
        3- Apagar a ultima tarefa
        4- Desfazer
        5- Listar tudo
        6- Sair
        """)
        print('-' * 50)
        try:
            menu = input("Escolha uma opção: ")
            if menu == '1':
                adiciona()
            elif menu == '2':
                lista()
            elif menu == '3':
                apaga()
            elif menu == '4':
                desfazer()
            elif menu == '5':
                lista_tudo()
            elif menu == '6':
                print("Bye, Bye!")
                menu = False
            elif menu != '':
                print('Algo deu errado, escolha outra opção ou aperte 5 para sair')
        except Exception:
            print("Algo deu errado")
            menu = False


menu()
