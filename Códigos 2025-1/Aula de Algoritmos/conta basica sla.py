tempo_total_min = int(input("Digite o tempo em minutos: "))

horas = tempo_total_min // 60
minutos = tempo_total_min % 60
segundos = 0

print(f"{tempo_total_min} minutos equivalem a: {horas}h {minutos}min {segundos}s")
