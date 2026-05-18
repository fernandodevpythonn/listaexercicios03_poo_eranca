from funcionario import Funcionario
class Pessoa:
    def __init__(self,nome="sem nome", perfil = "sem perfil", email = "sem email"):
        self.nome = nome
        self.perfil = perfil
        self.email = email
        self.__senha = 0
    