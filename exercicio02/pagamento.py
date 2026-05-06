
class pagamento:
    def __init__(self,valor_pagamento = 0,num_conta = 0):
        self.valor_pagamento = valor_pagamento
        self.num_conta = num_conta
    
    def realizar_compra(self):
        self.num_conta = float(input("Número da conta que receberá o pagamento: "))
        self.valor = float(input("valor do pagamento: "))