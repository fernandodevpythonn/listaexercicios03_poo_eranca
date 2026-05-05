from cliente import Cliente
from produtos import Produto
prod = Produto()

class Cliente_vip(Cliente):
        def __init__(self, nome="sem nome",email = "sem email", perfil = "sem perfil"):
            super().__init__(perfil,nome,email)
        def fazer_compra_cliente_vip(self):
                    opc = input("qual produto deseja comprar? ")
                    if opc in prod.produtos:
                        print(f"produto {prod.nome} disponivel")
                        print(f"valor promocao {prod.valor_promo}")
