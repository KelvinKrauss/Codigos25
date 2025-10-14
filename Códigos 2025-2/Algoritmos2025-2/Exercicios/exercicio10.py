n = int(input())
nd = 0
naoprimo = False
for i in range (1, n + 1):#3
    if n % i == 0:
        nd += 1
if nd == 1 or nd >=3:
        naoprimo = True
if naoprimo == True:
    print("nao primo")
else:
    print("é primo")
