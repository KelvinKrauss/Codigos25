lados = int(input("quantos lados tem o poligono? :"))
if lados > 10 or lados < 3:
    lados = ("NUMERO INVALIDO, insira um numero entre 3 e 10 ")
if lados == 3:
    lados = ("Triangulo")
if lados == 4:
    lados = ("Quadrado")
if lados == 5:
    lados = ("Pentágono")
if lados == 6:
    lados = ("Hexagono")
if lados == 7:
    lados = ("Heptagono")
if lados == 8:
    lados = ("Octogono")
if lados == 9:
    lados = ("Eneagono")
if lados == 10:
    lados = ("Decagono")    
    
print(f"o seu poligono é um {lados}")

