from utils import *
def menu():
  print("Lista de exercícios de POO - 04")
  print("1 - Exercício01")
  print("2 - Exercício02")
  print("3 - Exercício03")
  print("4 - Exercício04")
  print("5 - Fechar")
def main():
  while True:
   opc = input("Escolha um exercício: ")
   match opc:
    case "1":
      main01()
      input("Aperte Enter para voltar")
    case "2":
      main02()
      input("Aperte Enter para voltar")
    case "3":
      main03()
      input("Aperte Enter para voltar")
    case "4":
      main04()
      input("Aperte Enter para voltar")
    case "5":
      print("Sistema fechado")
      break
    case _:
       print("Valor inválido")
       break
if __name__ == "__main__":
  main()