def soma_pares(vetor):
    soma = 0
    for num in vetor:
        if num % 2 == 0:
            soma += num
    return soma

valores = []
for i in range(10):
    x = int(input(f"Digite o {i+1}º número: "))
    valores.append(x)

resultado = soma_pares(valores)
print("Soma dos pares:", resultado)
