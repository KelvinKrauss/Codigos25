s = float(input("Digite os segundos: "))
dias = int(s // (24 * 60 * 60))
s = s % (24 * 60 * 60)
horas = int(s // 3600)
s = s % 3600
minutos = int(s // 60)
segundos = int(s % 60)
print(dias, "dia(s),", horas, "hora(s),", minutos, "minuto(s),", segundos, "segundo(s)")
