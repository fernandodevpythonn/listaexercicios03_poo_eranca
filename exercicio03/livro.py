from .produto import Produto
class Livro(Produto):
    def __init__(self,nome="sem nome", valor= 0, tipo="livro"):
        super().__init__(nome,valor,tipo)
        self.livros = []
    @staticmethod
    def notificacao(nome):
        print(f"livro {nome} editado")
    def adicionar_livros(self):
        self.livros.append(self.nome)
        print(self.nome)
        print(f"livros: {self.livros}")
    def editar_livro(self):
       pass
