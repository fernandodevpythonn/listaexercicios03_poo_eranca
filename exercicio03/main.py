from produto import Produto
prod = Produto()
def menu():
    print("1 - Fazer login")
    print("2 - Cadastrar pessoa")
    print("3 - Cadastrar produto")
def main():
   prod.cadastrar_produto()

if __name__ == "__main__":
    main()