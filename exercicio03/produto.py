from livro import Livro
liv = Livro()
class Produto():
    def __init__(self,nome="sem nome", valor = 0, tipo="sem tipo"):
        self.nome = nome
        self.valor = valor
        self.tipo = tipo
    @staticmethod
    def notificacao(nome,tipo):
        print(f"Produto {nome} do tipo {tipo} cadastrado com sucesso!")
    def cadastrar_produto(self):
         self.nome = input("Nome do produto:")
         self.valor = float(input("Valor do produto: "))
         self.tipo = input("Tipo de produto(Eletrônico/Livro):")
         if self.tipo == "livro":
             liv.adicionar_livros(self.nome)
         if self.tipo == "eletronico" or self.tipo == "livro":
           Produto.notificacao(self.nome,self.tipo)
         else:
             raise ValueError("Erro: Produto inválido")