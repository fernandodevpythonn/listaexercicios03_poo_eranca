from funcionario import Funcionario
class Pessoa:
    def __init__(self,nome="sem nome", perfil = "sem perfil", email = "sem email"):
        self.nome = nome
        self.perfil = perfil
        self.email = email
        self.__senha = 0
    @staticmethod
    def validar_email(email):
        return "@" in email and "." in email
    @property
    def senha(self):
        return self.__senha
    @senha.setter
    def senha(self,valor):
        senha_pessoa = valor
        self.__senha = senha_pessoa
    def fazer_login(self):
        self.nome = input("Nome: ")
        if self.nome.isalpha():
            print(f"Nome {self.nome} cadastrado")
        self.perfil = input("Perfil")
        if self.perfil.isdigit():
            raise ValueError("Erro: Perfil inválido")
        self.email = input("Email: ")
        if not Pessoa.validar_email(self.email):
            raise ValueError("Email inválido")
        self.senha = input("Senha: ")