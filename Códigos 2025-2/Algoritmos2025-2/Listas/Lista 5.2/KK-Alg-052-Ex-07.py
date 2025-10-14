def Triangulo_valido(a, b, c):
    if a >= b + c or b >= a + c or c >= b + a:
        Triangulo = False
    else:
        Triangulo = True
    return Triangulo
        
print(Triangulo_valido(int(input("Digite o lado A : ")),int(input("Digite o lado B : ")),int(input("Digite o lado C : "))))