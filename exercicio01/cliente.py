#login e compras
from usuario import Usuario
from produtos import produto
prod = produto()

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
    def fazer_compra_cliente(self):
        if self.perfil == "cliente":
                    prod.mostrar_produtos_cliente()
                    opc = input("qual produto deseja comprar? ")
                    if self.perfil == "cliente" or self.perfil == "administrador":
                     if opc in prod.produtos:
                        print(f"produto {opc} disponivel")
                        print(f"valor original: {prod.valor_original}")
        else:
                    raise ValueError("erro: faça login primeiro")