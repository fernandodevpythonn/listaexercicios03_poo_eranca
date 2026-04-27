from usuario import Usuario

class produto(Usuario):

    def __init__(self, nome = "sem nome", valor_original = 0, valor_promo = 0, tipo = "sem tipo", perfil = "sem perfil"):
        super().__init__(perfil)
        self.nome = nome
        self.valor_original = valor_original
        self.valor_promo = valor_promo
        self.tipo = tipo
        self.produtos = {
           "produto": self.nome,
           "valorpromo": self.valor_promo,
           "valornormal": self.valor_original
        }

    def adicionar_produto(self):
         if self.perfil == "administrador" or "adm":
          self.nome = input("Nome: ")
          if self.nome.isalpha():
             print(f"{self.nome} cadastrado")
          else:
             raise ValueError("Erro: nome inválido")
          self.tipo = input("tipo(promocao/normal): ")
          if self.tipo.isalpha():
             print(f"{self.tipo} adicionado")
          else:
             raise ValueError("Erro: tipo inválido")
          try:
            if self.tipo == "normal":
               self.valor_original = float(input("Valor: "))
            elif self.tipo == "promocao":
               self.valor_promo = float(input("valor: "))
          except ValueError:
             print("Erro: valor de produto inválido")
         else:
            raise ValueError("erro: precisa ser administrador para acessar esta página")

    def mostrar_produtos(self):
        for chave,valor in self.produtos.items():
           print(chave)
           print(valor)
     