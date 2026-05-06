from notificacao import notificacao
from pagamento import pagamento

class pagamento_com_notificacao(notificacao,pagamento):
    def __init__(self, valor):
        pagamento.__init__(self, valor)
        notificacao.__init__(self)
    
    def enviar_notificacao(self):
        self.mostrar_notificacao(self.valor_pagamento)