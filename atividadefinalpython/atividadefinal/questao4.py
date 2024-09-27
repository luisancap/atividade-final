import random

animais = {
    "Mamíferos": ["elefante", "leão", "tigre", "gato", "cachorro"],
    "Aves": ["papagaio", "águia", "canário", "pomba", "coruja"],
    "Répteis": ["cobra", "jacaré", "lagarto", "iguana", "crocodilo"],
    "Peixes": ["salmão", "tubarão", "tilápia", "badejo", "bacalhau"],
    "Anfíbios": ["sapo", "rã", "salamandra", "perereca", "axolote"]
}

def exibir_categorias():
    print("===== JOGO DE ADIVINHAÇÃO DE PALAVRAS =====")
    print("Escolha uma categoria de animais:")
    for i, categoria in enumerate(animais.keys(), 1):
        print(f"{i} - {categoria}")
    print()

def escolher_categoria():
    while True:
        try:
            escolha = int(input("Digite o número da categoria desejada: "))
            if 1 <= escolha <= len(animais):
                categoria_escolhida = list(animais.keys())[escolha - 1]
                return categoria_escolhida
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

def jogo_de_adivinhacao():
    exibir_categorias()

    categoria = escolher_categoria()
    print(f"\nCategoria escolhida: {categoria}")

    palavra_sorteada = random.choice(animais[categoria])
    letras_palavra = len(palavra_sorteada)

    palpites = []

    print("------- Vamos Iniciar o Jogo! --------------")
    print(f"Dica: A palavra tem {letras_palavra} letras.")

    while True:
        palpite = input("Tente adivinhar a palavra: ").lower().strip()

        palpites.append(palpite)

        if palpite == palavra_sorteada:
            print("\nParabéns! Você acertou a palavra.")
            break
        else:
            print("Palpite incorreto. Tente novamente.")
            print(f"Dica: A palavra tem {letras_palavra} letras.")

    print("--------------------------------------------")
    print(f"Número de palpites: {len(palpites)}")
    print(f"Palpites realizados: {palpites}")

jogo_de_adivinhacao()
