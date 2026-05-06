#login e compras
from produtos import Produto
from usuario import Usuario
prod = Produto()

class Cliente(Usuario):
    def __init__(self,nome = "sem nome",email = "sem email",perfil="sem perfil"):
       super().__init__(perfil,nome,email)
    @staticmethod

    def validar_perfil(self):
        if self.perfil == "cliente":
            print("( cliente )")
            return True
        
    def fazer_compra_cliente(self):
                    print(prod.nome)
                    opc = input("qual produto deseja comprar? ")
                    if self.perfil == "cliente":
                     if opc == prod.nome:
                        print(f"produto {opc} disponivel")
                        print(f"valor original: {prod.valor_original}")
