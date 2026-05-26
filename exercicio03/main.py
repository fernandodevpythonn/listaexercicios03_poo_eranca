from pessoa import Pessoa
from produto import Produto
from livro import Livro
liv = Livro()
pess = Pessoa()
prod = Produto()
def menu():
    print("1 - Fazer login")
    print("2 - Mostrar pessoa")
    print("3 - Cadastrar produto")
    print("4 - Mostrar produto")

def main():
   while True:
       menu()
       opc = input("opção: ")
       match opc:
            case "1":
               pess.fazer_login()
            case "2":
               pess.mostrar_pessoa()
            case "3":
                # if pess.perfil == "administrador":
                   prod.cadastrar_produto()
                   if prod.tipo == "livro":
                       liv.adicionar_livros()
                # else:
                #     raise ValueError("Erro: precisa ser um administrador para cadastrar um produto.")
            case "4":
               prod.mostrar_produtos()
if __name__ == "__main__":
    main()