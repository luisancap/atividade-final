import sys

funcionarios = []

def adicionar_funcionario():

    nome = input("Digite o nome do funcionário: ")
    idade = input("Digite a idade do funcionário: : ")
    cargo = input("Digite o cargo do funcionário: ")

    funcionario = {
        "nome": nome,
        "idade": idade,
        "cargo": cargo
    }
    funcionarios.append(funcionario)

    print(f"\nTarefa adicionada com sucesso!\n")

def exibir_funcionarios():
    if len(funcionarios) > 0:
        for i, funcionario in enumerate(funcionarios, 1):
            print(f"{i}-{funcionario['nome']}: idade: {funcionario['idade']}, cargo: {funcionario['cargo']}\n")
    else:
        print("Sem funcionarios!")

def buscar_funcionario():
    cargo = input("Digite o cargo que deseja buscar: ")
    for funcionario in funcionarios:
        if funcionario["cargo"] == cargo:
            print(f"Funcionários com o cargo '{funcionario["cargo"]}' -:\n")
            print(f"Nome: {funcionario["nome"]}, Idade: {funcionario["idade"]}")
            return

def main():
    while True:
        print("================ GERENCIADOR DE TAREFAS =====================\n")
        funcao = int(input("ESCOLHA UMA OPÇÃO:\n1-Adicionar funcionario\n2-Exibir funcionarios\n3-buscar funcionarios\n4-Sair\n"))

        match funcao:
            case 1:
                adicionar_funcionario()
            case 2:
                exibir_funcionarios()
            case 3:
                buscar_funcionario()
            case 4:
                sys.exit()

main()
