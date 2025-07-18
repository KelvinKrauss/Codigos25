matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("Matriz:")
for linha in matriz:
    print(linha)

soma_diagonal = 0
for i in range(3):
    soma_diagonal += matriz[i][i]

print("Soma da diagonal principal:", soma_diagonal)