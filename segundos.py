total_segs = int(input("Por favor, emtre com, o número de segundos que deseja converter: "))

horas = total_segs // 3600
dias = horas // 24
horas_restantes = horas - dias * 24
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(dias, "dias,", horas_restantes, "horas,", minutos, "minutos e", segs_restantes_final, "segundos")
