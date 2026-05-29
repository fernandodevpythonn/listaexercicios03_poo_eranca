from .pessoa import Pessoa
class Suporte(Pessoa):
    def __init__(self,nome,perfil):
        self.problema = ""
        self.solucao = ""
        self.cliente = ""
        self.dispositivo = ""
        self.problemas = []
        super().__init__(nome,perfil)
    def adicionar_problema(self):
        print("Adicionando problema:")
        self.problema = input("Problema: ")
        self.problemas.append(self.problema)
        self.dispositivo = input("Dispositivo: ")
        self.cliente = input("Cliente: ")
    def mostrar_problemas(self):
        print(f"problemas: {self.problemas}")
    def orientacao(self):
        prob = input("Problema: ")
        if prob in self.problemas:
         self.solucao = input("Orientação: ")
         print(f"Solução para {self.problema} é {self.solucao}")
