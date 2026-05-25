from produto import Produto
class Eletronico(Produto):
    def __init__(self,nome, valor, tipo):
        super().__init__(nome,valor,tipo)
    @staticmethod
    def mostrar_produto(self):
        print(self.nome)
