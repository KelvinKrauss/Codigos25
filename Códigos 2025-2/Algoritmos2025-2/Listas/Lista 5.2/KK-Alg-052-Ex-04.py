def mediana(a,b,c):
        lista = [a, b, c]
        lista.sort()
        return lista[1],a,b,c

mediana, a, b, c = mediana(int(input("Digite A : ")),int(input("Digite B :")),int(input("Digite C : ")))
print(f"a mediana entre {a}, {b}, {c}, é {mediana}!")