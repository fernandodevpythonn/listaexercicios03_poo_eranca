class Cliente(usuario):
    def __init__(self,nome,senha,email):
        super().__init__(nome,senha,email)
        self.__senha = ""
        self.__cpf = 0
    @staticmethod
    def validar_email(email):
        return "@" in email and ".com" in email