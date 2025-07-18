#edaedaed
def contar_partes():
    # Solicitar entrada do usuário
    texto = input("Digite uma string: ")
    separador = input("Digite o caracter separador: ")
    
    # Inicializar contador (sempre há pelo menos 1 parte)
    contador = 1
    
    # Percorrer cada caracter da string
    for caractere in texto:
        if caractere == separador:
            contador += 1
    
    # Exibir resultado
    print(f"{contador} partes")

# Chamar a função
contar_partes() 