class Usuario:
    def __init__(self, nome = "sem nome", email = "sem email",  perfil = "sem perfil"):
        self.nome = nome
        self.email = email
        self.perfil = perfil
        self.__cpf = 0
        self.__senha = ""
    @staticmethod
    def validar_email(email):
        return "@" in email and ".com" in email and ("gmail" in email) or ("hotmail" in email)

    @property
    def senha(self):
        return self.__senha
    @senha.setter
    def senha(self,valor):
        senha_usu = valor
        self.__senha = senha_usu
    
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self,valor):
        if len(valor) == 11:
            cpf_cli = valor
            self.__cpf = cpf_cli
        else:
            raise ValueError("Erro: tamanho de senha inválido")
        
    def enviar_mensagem_boas_vindas(self):
      print(f"olá {self.nome} seja bem vindo(a)")

    def realizar_login(self):
        self.email = input("Email: ")
        if self.email.isalpha():
            print(f"email{self.email} cadastrado")
        self.senha = input("Senha: ")
        print(f"senha {self.senha} cadastrada")