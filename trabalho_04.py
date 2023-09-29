# Variável global para o ID
id_global = 0

# Lista vazia criada para armazenar os colaboradores
lista_colaboradores = []

# Função usada para cadastrar um colaborador
def cadastrar_colaborador(id):
    global id_global
    print('\n'
          '--------------------------- MENU DE CADASTRAMENTO DE COLABORADORES ---------------------------\n'
          ' ')
    nome = input("Digite o nome do colaborador: ")
    setor = input("Digite o setor do colaborador: ")
    salario = float(input("Digite o salário do colaborador: "))

    colaborador = {
        "ID": id,
        "Nome": nome,
        "Setor": setor,
        "Salário": salario
    }

    lista_colaboradores.append(colaborador)
    id_global += 1

# Função para consultar colaboradores
def consultar_colaborador():
    while True:
        print('\n'
            '------------------------------- MENU DE CONSULTA DE COLABORADORES ------------------------------')
        print("\nOpções de consulta:")
        print("1. Consultar Todos")
        print("2. Consultar por ID")
        print("3. Consultar por Setor")
        print("4. Retornar ao menu")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            for colaborador in lista_colaboradores:
                print(' \n'
                      f"ID: {colaborador['ID']}\n"
                      f"Nome: {colaborador['Nome']}\n"
                      f"Setor: {colaborador['Setor']}\n"
                      f"Salário: {colaborador['Salário']}\n"
                      ' '
                      )
        elif opcao == "2":
            id_consulta = int(input("Digite o ID do colaborador a ser consultado: "))
            encontrado = False
            for colaborador in lista_colaboradores:
                if colaborador["ID"] == id_consulta:
                    print(' \n'
                      f"ID: {colaborador['ID']}\n"
                      f"Nome: {colaborador['Nome']}\n"
                      f"Setor: {colaborador['Setor']}\n"
                      f"Salário: {colaborador['Salário']}\n"
                      ' '
                      )
                    encontrado = True
                    break
            if not encontrado:
                print("Colaborador não encontrado.")
        elif opcao == "3":
            setor_consulta = input("Digite o setor a ser consultado: ")
            encontrados = [colaborador for colaborador in lista_colaboradores if colaborador["Setor"] == setor_consulta]
            if encontrados:
                for colaborador in encontrados:
                    print(' \n'
                      f"ID: {colaborador['ID']}\n"
                      f"Nome: {colaborador['Nome']}\n"
                      f"Setor: {colaborador['Setor']}\n"
                      f"Salário: {colaborador['Salário']}\n"
                      ' '
                      )
            else:
                print("Nenhum colaborador encontrado para o setor especificado.")
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")

# Função para remover um colaborador
def remover_colaborador():
    print('\n'
        '------------------------------- MENU DE REMOÇÃO DE COLABORADORES -------------------------------')
    id_remover = int(input("Digite o ID do colaborador a ser removido: "))
    encontrado = False
    for colaborador in lista_colaboradores:
        if colaborador["ID"] == id_remover:
            lista_colaboradores.remove(colaborador)
            print("Colaborador removido com sucesso.")
            encontrado = True
            break
    if not encontrado:
        print("Colaborador não encontrado.")

# Função principal
def main():
    print("------ Bem-vindo ao sistema de gerenciamento de pessoas do Erivelton Felipe de Oliveira! ------")

    while True:
        print("\nOpções do menu principal:")
        print("1. Cadastrar Colaborador")
        print("2. Consultar Colaborador")
        print("3. Remover Colaborador")
        print("4. Encerrar Programa")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_colaborador(id_global)
        elif opcao == "2":
            consultar_colaborador()
        elif opcao == "3":
            remover_colaborador()
        elif opcao == "4":
            print("Encerrando o programa. Obrigado!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
