#edaedaed
def contar_partes():
   
    texto = input("Digite uma string: ")
    separador = input("Digite o caracter separador: ")
    
    
    contador = 1
    
    
    for caractere in texto:
        if caractere == separador:
            contador += 1
    
   
    print(f"{contador} partes")


contar_partes() 