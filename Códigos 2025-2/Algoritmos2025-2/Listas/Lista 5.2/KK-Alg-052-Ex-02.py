def taxi(km):#1km = 1000,1,4km = 1400 metros = 2,50
    metros = km
    valor = 4
    metros = metros * 1000
    preco = (metros // 140)
    valor = valor + preco * 0.25
    return valor
    
valor = taxi(float(input("Digite os kilometros percorridos :")))
print(f"o valor é {valor} R$")