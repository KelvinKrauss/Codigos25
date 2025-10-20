def hex2int(hex):
    if hex.isdigit():
        print (hex)
    else:
        hex = hex.upper()
        caracteres_hex = ["A","B","C","D",'E','F']
        if hex in caracteres_hex:
            posicao = caracteres_hex.index(hex)
            print(posicao + 10)

def int2hex(decimal):#0 a 15
    decimal_numero = int(decimal)
    if decimal_numero <=9:
        print(decimal)
    elif decimal >= 10:
        
        

#hex2int(str(input("Digito Hexadecimal : ")))
int2hex(str(input("Digito Decimal : ")))