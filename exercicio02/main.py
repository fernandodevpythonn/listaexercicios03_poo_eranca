from .pagamento_com_notificacao import Pagamento_com_notificacao
pag = Pagamento_com_notificacao(0,"sem produto")
def menu():
  print("1 - adicionar produto")
def main02():
  while True:
    menu()
    opc = input("opção: ")
    match opc:
      case "1":
        produto = input("produto: ")
        valor = float(input("valor: "))
        pag = Pagamento_com_notificacao(valor,produto)
        pag.rodar()
