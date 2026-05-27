
class Pagamento:
    def __init__(self,valor_pagamento,produto):
        self.valor_pagamento = valor_pagamento
        self.produto = produto
    def realizar_pagamento(self):
        print(f"{self.produto} no valor de R${self.valor_pagamento:,.2f} pago")
