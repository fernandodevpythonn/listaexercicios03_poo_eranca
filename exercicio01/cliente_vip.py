from cliente import Cliente
from produtos import produto
prod = produto()
class Cliente_vip(Cliente):
        def __init__(self, nome="sem nome",email = "sem email", perfil = "sem perfil", senha = 0):
              super().__init__(nome,perfil,email,senha)
        def fazer_compra_cliente_vip(self):
                if self.perfil == "cliente vip":
                    prod.mostrar_produtos_cliente_vip()
                    opc = input("qual produto deseja comprar? ")
                    if opc in prod.produtos:
                        print(f"produto {prod.nome} disponivel")
                        print(f"valor promocao {prod.valor_promo}")
                else:
                    raise ValueError("erro: faça login primeiro")