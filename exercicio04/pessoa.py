class Pessoa:
    def __init__(self, nome, perfil, email, senha):
        self.nome = nome
        self.perfil = perfil
        self.email = email
        self.senha = senha
    def login(self):
        print(f"Login  realizado - Nome: {self.nome}, email: {self.email}, perfil: {self.perfil}")
    def mostrar_pessoa(self):
        print(f"Pessoa: {self.nome}, Perfil: {self.perfil}")