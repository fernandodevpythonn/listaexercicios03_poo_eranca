class Eletronico:
    def __init__(self,nome = "sem nome", valor = 0, tipo = "eletronico"):
        self.nome = nome
        self.valor = valor
        self.tipo = tipo
    @staticmethod
    def notificacao(nome):
        print(f"Produto {nome} cadastrado com sucesso!")
    def cadastrar_produto(self):
        self.nome = input("Nome do produto:")
        self.valor = float(input("Valor do produto: "))
        Eletronico.notificacao(self.nome)
    