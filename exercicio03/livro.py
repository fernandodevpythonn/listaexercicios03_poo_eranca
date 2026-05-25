class Livro:
    def __init__(self,nome, valor, tipo):
        super().__init__(nome,valor,tipo)
        self.livros = []
    @staticmethod
    def notificacao(nome):
        pass
    def adicionar_livros(self,livro):
        self.livros.append(livro)
    def editar_livro(self):
        pass