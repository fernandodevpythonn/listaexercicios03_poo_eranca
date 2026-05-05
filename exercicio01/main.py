from usuario import Usuario
from produtos import Produto

from cliente_vip import Cliente_vip
from cliente import Cliente
clivip = Cliente_vip()
cli = Cliente()
prod = Produto()
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
                  prod.mostrar_produtos_cliente()
                  cli.fazer_compra_cliente()
                elif usu.perfil == "cliente vip":
                  prod.mostrar_produtos_cliente_vip()
                  clivip.fazer_compra_cliente_vip()
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
                  if usu.perfil == "cliente":
                    prod.mostrar_produtos_cliente()
                  elif usu.perfil == "cliente vip":
                    prod.mostrar_produtos_cliente_vip()
                  else:
                    prod.mostrar_produtos()
                else:
                    print("nenhum produto cadastrado")

if __name__ == "__main__":
    main()