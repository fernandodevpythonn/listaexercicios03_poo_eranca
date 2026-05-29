from .pessoa import Pessoa
class Tecnico(Pessoa):
    def __init__(self,nome,perfil):
        super().__init__(nome,perfil)
        self.dispositivo = ""
        self.cliente = ""
        self.agenda = ""
        self.agendas = []
        self.clientes = []
    def agendar(self,problema):
        self.agenda = input("Data")
        self.agendas.append(self.agenda)
        cli = input("Cliente: ")
        self.clientes.append(cli)
        if cli in self.clientes:
         print(f"Visita de {self.nome} marcada para {self.agenda}, com o cliente {cli} para resolver o problema de {problema}")
    def mostrar_agendas(self):
       print(f"Agendas: {self.agendas}")

