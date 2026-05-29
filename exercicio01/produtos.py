from .usuario import Usuario

class Produto(Usuario):

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
             self.produtos["produto"] = self.nome
             print(f"{self.nome} cadastrado")
          else:
             raise ValueError("Erro: nome inválido")
          try:
               self.valor_original = float(input("Valor original: "))
               self.produtos["valornormal"] = self.valor_original
               self.valor_promo = float(input("valor promoção: "))
               if self.valor_promo <= self.valor_original:
                self.produtos["valorpromo"] = self.valor_promo
               else:
                  ValueError("erro: valor de promoção precisa ser menor que o preço original")
          except ValueError:
             print("Erro: valor de produto inválido")
         else:
            raise ValueError("erro: precisa ser administrador para acessar esta página")

    def mostrar_produtos_cliente(self):
       print(f"{self.produtos["produto"]}, {self.produtos["valornormal"]}")
    def mostrar_produtos_cliente_vip(self):
       print(f"{self.produtos["produto"]}, {self.produtos["valorpromo"]}")
    def mostrar_produtos(self):
        print(f"{self.produtos["produto"]}, promoção: {self.produtos["valorpromo"]}, normal: {self.produtos["valornormal"]}")