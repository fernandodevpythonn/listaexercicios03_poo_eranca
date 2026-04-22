#login e compras

class Cliente:
    def __init__(self,nome = "sem nome",email = "sem email",perfil="sem perfil"):
       self.nome = nome
       self.__senha = 0
       self.email = email
       self.perfil = perfil
    
    def mostrar_cliente(self):
        print(f"nome: {self.nome}")