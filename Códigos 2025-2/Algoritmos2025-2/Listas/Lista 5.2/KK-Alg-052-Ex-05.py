def numeros_ordinais(n):
    lista = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto", "Sexto", "Sétimo","Oitavo","Nono","Décimo", "Décimo Primeiro", "Décimo Segundo"]
    if n > 13 or n < 1:
        print("")
    else:
        print(lista[n - 1])


numeros_ordinais(int(input("Digite o nome que você quer o nome em ordinal : ")))