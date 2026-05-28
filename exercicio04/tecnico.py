from pessoa import Pessoa
class Tecnico(Pessoa):
    def __init__(self,nome,idade,perfil,senha):
        super().__init__(nome,idade,perfil,senha)
        self.dispositivo = ""
        self.cliente = ""
    def mostrar_problema(self,cliente,dispositivo):
        print(f"Problema com o {dispositivo} do(a) {cliente}, Técnico: {self.nome}")
    
tec = Tecnico("lucas",20,"suporte",12345)
tec.login()
tec.mostrar_problema("Vitor", "celular")