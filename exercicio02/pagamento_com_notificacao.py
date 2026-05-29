from .pagamento import Pagamento
from .notificacao import Notificacao
class Pagamento_com_notificacao(Pagamento,Notificacao):
  def __init__(self, valor_pagamento,produto):
    Pagamento.__init__(self,valor_pagamento,produto)
    Notificacao.__init__(self)
  
  def rodar(self):
    self.realizar_pagamento()
    self.notificar()

