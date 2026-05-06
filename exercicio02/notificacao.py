class notificacao():
    def __init__(self,notificacao = "sem notificacao"):
        self.notificacao = notificacao

    def mostrar_notificacao(self,valor):
        self.notificacao = (f"pagamento de {valor} reais efetuado")