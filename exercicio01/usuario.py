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

    def enviar_mensagem_boas_vindas(self):
      print(f"olá {self.nome} seja bem vindo(a)")

    