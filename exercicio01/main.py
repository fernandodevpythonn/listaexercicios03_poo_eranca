from usuario import Usuario
from produtos import produto

from cliente_vip import Cliente_vip
clivip = Cliente_vip()

prod = produto()
usu = Usuario()

def menu():
    print("1 - Fazer login")
    print("2 - Fazer compras")
    print("3 - Cadastrar produto")
    print("4 - mostrar usuário")
    print("5 - mostrar produtos")

def main():
    while True:
        menu()
        opcao = input("opção: ")
        match opcao:
            case "1":
                usu.realizar_login()
            case "2":
                if usu.perfil == "cliente":
                    prod.mostrar_produtos()
                    opc = input("qual produto deseja comprar? ")
                    if opc in prod:
                        print(f"produto {prod.nome} disponivel")
                        print(f"valor original: {prod.valor_original}")
                elif usu.perfil == "cliente vipe":
                    prod.mostrar_produtos()
                    opc = input("qual produto deseja comprar? ")
                    if opc in prod:
                        print(f"produto {produto} disponivel")
                        print(f"valor promocao {prod.valor_promo}")
                else:
                    raise ValueError("erro: faça login primeiro")
            case "3":
                 if usu.perfil == "administrador" or "adm":
                   prod.adicionar_produto()
                 else:
                    raise ValueError("erro: precisa ser administrador para acessar esta página")
            case "4":
                if usu.perfil == "administrador" or usu.perfil == "cliente" or usu.perfil == "cliente vip":
                  usu.mostrar_usuario()
                else:
                    raise ValueError("erro: perfil inválido")
            case "5":
                if prod.nome != "sem nome":
                 prod.mostrar_produtos()
                else:
                    print("nenhum produto cadastrado")

if __name__ == "__main__":
    main()