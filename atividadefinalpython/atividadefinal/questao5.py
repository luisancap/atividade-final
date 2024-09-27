import sys

lista_de_tarefas = []
ultimo_id = 0

def adicionar_tarefas():
    global ultimo_id
    key = input("Digite a descrição da tarefa: ")
    prioridade = input("Insira a prioridade (Alta - A, Média - M, Baixa - B): ").lower()

    if prioridade in ['a', 'm', 'b']:
        ultimo_id += 1
        tarefa = {
            "id": ultimo_id,
            "descricao": key,
            "prioridade": prioridade
        }
        lista_de_tarefas.append(tarefa)
        print(f"\nTarefa adicionada com sucesso!\n")
    else:
        print("Não foi possível adicionar a tarefa!\n")

def exibir_tarefas():
    if len(lista_de_tarefas) > 0:
        print("\nTarefas de alta prioridade:")
        for tarefa in lista_de_tarefas:
            if tarefa["prioridade"] == "a":
                print(f"{tarefa['id']} - {tarefa['descricao']}")

        print("\nTarefas de média prioridade:")
        for tarefa in lista_de_tarefas:
            if tarefa["prioridade"] == "m":
                print(f"{tarefa['id']} - {tarefa['descricao']}")

        print("\nTarefas de baixa prioridade:")
        for tarefa in lista_de_tarefas:
            if tarefa["prioridade"] == "b":
                print(f"{tarefa['id']} - {tarefa['descricao']}")
    else:
        print("Lista vazia!\n")

def concluir_tarefa():
    try:
        id_tarefa = int(input("Digite o ID da tarefa a ser concluída: "))
        for tarefa in lista_de_tarefas:
            if tarefa["id"] == id_tarefa:
                lista_de_tarefas.remove(tarefa)
                print(f"\nTarefa '{tarefa["descricao"]}'concluída com sucesso!\n")
                return
        print("\nTarefa com o ID fornecido não foi encontrada!\n")
    except ValueError:
        print("\nID inválido! Insira um número.\n")

def main():
    while True:
        print("================ GERENCIADOR DE TAREFAS =====================\n")
        funcao = int(input("ESCOLHA UMA OPÇÃO:\n1-Adicionar Tarefa\n2-Exibir tarefas\n3-Concluir tarefa\n4-Sair\n"))

        match funcao:
            case 1:
                adicionar_tarefas()
            case 2:
                exibir_tarefas()
            case 3:
                concluir_tarefa()
            case 4:
                sys.exit()

main()
