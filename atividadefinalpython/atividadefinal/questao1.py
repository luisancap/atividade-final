lista = []
infinito = float("inf")
soma = 0
dias_frios = 0
max_temp = 0
min_temp = infinito

print("========== TEMPERATURAS DIÁRIAS =========\n")
for i in range(10):
    temperaturas = float(input(f"Insira as temperatura do {i+1} dia: "))
    lista.append(temperaturas)
    soma += temperaturas

media = soma / len(lista)

for i in range(10):
    if lista[i] < media:
        dias_frios += 1
    if lista[i] > max_temp:
        max_temp = lista[i]
    if lista[i] < min_temp:
        min_temp = lista[i]
print("============= Resultado =================\n")
print(f"Menor temperatura: {min_temp}")
print(f"Maior temperatura: {max_temp}")
print(f"Temperatura média: {media}")
print(f"Número de dias com temperatura abaixo da média: {dias_frios}")
