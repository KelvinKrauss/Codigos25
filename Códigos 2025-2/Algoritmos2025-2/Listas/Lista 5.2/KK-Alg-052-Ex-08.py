text = str(input())
proximaletramaiuscula = False
texto = []
for char in texto:
    if proximaletramaiuscula == True:
        char = char.upper()
        texto.append(char)
        print (char)
        proximaletramaiuscula = False
    if char in (".","!","?"):
        proximaletramaiuscula = True

print(textomaiusculo)