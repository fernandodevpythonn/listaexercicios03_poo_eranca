from pessoa import Pessoa
class Suporte(Pessoa):
    def __init__(self,nome,idade,perfil,senha):
        super().__init__(nome,idade,perfil,senha)
        self.problema = ""
        self.cliente = ""
    def adicionar_problema(self):
        self.problema = input("problema: ")
        self.cliente = input("cliente: ")
    def mostrar_problema(self):
        print(f"Problema em {self.problema}, com a pessoa {self.cliente}")
sup = Suporte("lucas",20,"suporte",12345)
sup.login()
sup.adicionar_problema()
sup.mostrar_problema()