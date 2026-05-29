class Pessoa:
    def __init__(self, nome, perfil):
        self.nome = nome
        self.perfil = perfil
    def info(self):
        print(f"Nome: {self.nome}, perfil: {self.perfil}")
    