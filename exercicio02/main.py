from pagamento import pagamento
pag = pagamento()
from pagamento_com_notificacao import pagamento_com_notificacao
pag_com_not = pagamento_com_notificacao()

def menu():
    print("1 - Realizar pagamento")

def main():
    while True:
        menu()
        opc = input("escolha uma opção: ")
        match opc:
            case "1":
                pag.realizar_compra()
                pag_com_not.enviar_notificacao()
if __name__ == "__main__":
    main()