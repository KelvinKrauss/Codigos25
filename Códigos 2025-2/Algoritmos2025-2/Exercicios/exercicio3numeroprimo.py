numerosdivisiveis = 0
primo = False
n = int(input("digite o numero"))
for i in range (1, n + 1):
    if n % i == 0:
        numerosdivisiveis = numerosdivisiveis + 1
if numerosdivisiveis <= 2 and numerosdivisiveis != 1:
    primo = True

if primo == True:
    print(f"{n} é primo")
else:
    print(f"{n} nao é primo")