from .suporte import Suporte
from .tecnico import Tecnico
tec = Tecnico("sem nome", "sem perfil")
sup = Suporte("sem nome","sem perfil")#como faço para instanciar
login = False
def menu():
  print("1 - Fazer login")
  print("2 - mostrar problemas")
  print("3 - Adicionar problema(suporte)")
  print("4 - Mostrar pessoa")
  print("5 - Orientações(Suporte)")
  print("6 - Agendar(Técnico)")
  print("7 - Agendas")
def main04():
  while True:
    menu()
    opc = input("opção: ")
    match opc:
        case "1":
         try:
          nome = input("nome: ")
          perfil = input("perfil: ")
          if perfil == "suporte":
           sup = Suporte(nome,perfil)
          elif perfil == "tecnico":
           tec = Tecnico(nome,perfil)
          else:
           raise ValueError("Erro: perfil inválido")
         finally:
          login = True
        case "2":
         if login:
          if sup.perfil == "suporte":
           sup.mostrar_problemas()
          elif tec.perfil == "tecnico":
           sup.mostrar_problemas()
          else:
           raise ValueError("erro: usuário inválido")
          
        case "3":
         if login:
          print("problema")
          sup.adicionar_problema()
        case "4":
         if login:
          sup.info()
        case "5":
         if login:
          if sup.perfil == "suporte":
           sup.orientacao()
        case "6":
          if login:
           probl = input("Problema: ")
           if probl in sup.problemas:
            tec.agendar(probl)
