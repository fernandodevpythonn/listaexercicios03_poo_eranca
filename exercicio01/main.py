def menu():
    print("1 - Fazer login")
    print("2 - Fazer compras")
    print("3 - Cadastrar produto")
def main():
    while True:
        menu()
        opcao = input("opção: ")
        match opcao:
            case "1":
                pass