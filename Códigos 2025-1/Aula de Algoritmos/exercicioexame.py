#manipulação de string, botar o while pra ficar num loop, definir texto e definir quantidade de 'algoritmos'

while True:
    texto = input("digite aqui o texto")
    quantidadedea = texto.count("algoritmos")
    if quantidadedea > 0:
        print(f"tem essa quantidade de algoritmos no seu texto: {quantidadedea}")
    else:
        print("tem NADA")

