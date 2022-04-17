class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está a comer...')
            return

        print(f'{self.nome} está comendo {alimento}...')
        self.comendo=True

    def parar_comer(self):
        if not self.comendo:
            print(f' {self.nome} não está a comer...')
            return

        print(f'{self.nome} parou da de comer...')
        self.comendo=False
