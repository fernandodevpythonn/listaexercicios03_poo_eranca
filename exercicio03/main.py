from pessoa import Pessoa
# from produto import Produto
pess = Pessoa()
# prod = Produto()
def menu():
    print("1 - Fazer login")
    print("3 - Cadastrar produto")
def main():
   while True:
       menu()
       opc = input("opção: ")
       match opc:
           case "1":
               pess.fazer_login()

if __name__ == "__main__":
    main()