def preco_envio_e_commerce(itens):
    preco = 10.95
    for _ in range(itens):
        preco = preco + 2.95
    return preco - 2.95

preco = preco_envio_e_commerce(int(input("Digite a quantidade de itens : ")))
print(f"O custo de envio é {preco:.2f} R$")