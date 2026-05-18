class Livro:
    def __init__(self,nome = "sem nome", valor = 0.0, tipo = "Livro"):
        self.nome = nome
        self.valor = valor
        self.tipo = tipo
    @staticmethod
    def notificacao(nome):
        print(f"Livro {nome} cadastrado com sucesso!")

    def cadastrar_livro(self):
        self.nome = input("Nome do Livro: ")
        self.valor = float(input("Valor: "))
        Livro.notificacao(self.nome)