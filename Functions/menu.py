from Functions.adicionar import adicionar_membro, adicionar_cases, adicionar_disciplinas
from Functions.editar import editar_membro, editar_case, editar_disciplina
from Functions.listar import listar_membros, listar_disciplinas, listar_cases
from Functions.deletar import deletar_membro, deletar_disciplina, deletar_case

def menu_principal():
    while True:
        print("\nMenu Principal")
        print("1. Criar")
        print("2. Editar")
        print("3. Visualizar")
        print("4. Deletar")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            menu_criar()
        elif escolha == "2":
            menu_editar()
        elif escolha == "3":
            menu_visualizar()
        elif escolha == "4":
            menu_deletar()
        elif escolha == "5":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_criar():
    while True:
        print("\nMenu Criar")
        print("1. Time")
        print("2. Cases")
        print("3. Disciplinas")
        print("4. Voltar")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_membro()
        elif escolha == "2":
            adicionar_cases()
        elif escolha == "3":
            adicionar_disciplinas()
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_editar():
    while True:
        print("\nMenu Editar")
        print("1. Time")
        print("2. Cases")
        print("3. Disciplinas")
        print("4. Voltar")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            editar_membro()
        elif escolha == "2":
            editar_case()
        elif escolha == "3":
            editar_disciplina()
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_visualizar():
    while True:
        print("\nMenu Visualizar")
        print("1. Time")
        print("2. Cases")
        print("3. Disciplinas")
        print("4. Voltar")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            listar_membros()
        elif escolha == "2":
            listar_cases()
        elif escolha == "3":
            listar_disciplinas()
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_deletar():
    while True:
        print("\nMenu Deletar")
        print("1. Time")
        print("2. Cases")
        print("3. Disciplinas")
        print("4. Voltar")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            deletar_membro()
        elif escolha == "2":
            deletar_case()
        elif escolha == "3":
            deletar_disciplina()
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")
