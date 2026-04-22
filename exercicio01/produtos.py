class produto:
    def __init__(self, nome = "sem nome", valor_original = 0, valor_promo = 0, tipo = "sem tipo"):
        self.nome = nome
        self.valor_original = valor_original
        self.valor_promo = valor_promo
        self.tipo = tipo
    def adicionar_produto(self):
         self.nome = input("Nome: ")
         if self.nome.isalpha():
             print(f"{self.nome} cadastrado")
         else:
             raise ValueError("Erro: nome inválido")
         self.tipo = input("tipo: ")
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