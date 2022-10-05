time1 = input("Gols do time 1")
time2 = input("Gols do time 2")

if time1 > time2:
    print(f"Vitoria do time 1 por {time1} a {time2}")
elif time2 > time1:
    print(f"Vitoria do time 2 por {time2} a {time1}")
else:
    print(f"Empate por {time1} a {time2}")