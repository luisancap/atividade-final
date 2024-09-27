assentos = {1: True, 2: True, 3: True, 4: True, 5: True}

print("#======= SISTEMA DE RESERVA =======\n")

print(f"Assentos disponíveis: {list(assentos.keys())}")
reserva = int(input("Insira o assento desejado: "))

if reserva not in assentos:
    print(f"Desculpe, o assento {reserva} já está reservado ou não existe.\n")
else:
    del assentos[reserva]
    print(f"Assento {reserva} reservado com sucesso!")

    print(f"Assentos disponíveis: {list(assentos.keys())}")
