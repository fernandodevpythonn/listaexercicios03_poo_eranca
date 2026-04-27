#login e compras
from usuario import Usuario
class Cliente(Usuario):
    def __init__(self,nome = "sem nome",email = "sem email",perfil="sem perfil",senha = 0):
       super().__init__(perfil,nome,email,senha)
    @staticmethod
    def validar_perfil(self):
        if self.perfil == "cliente":
            print("( cliente )")
            return True
    def mostrar_cliente(self):
        print(f"nome: {self.nome}")