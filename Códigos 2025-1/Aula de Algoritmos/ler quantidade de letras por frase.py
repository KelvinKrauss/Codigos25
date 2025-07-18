frase = input("Digite uma frase: ")

cont = 0
for letra in frase:
    if letra.lower() == 'a':
        cont += 1

print("Quantidade de letras 'a':", cont)