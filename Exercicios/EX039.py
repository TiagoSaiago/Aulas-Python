import time

equipas = (
    "Real Madrid", "Girona", "Atl.Madrid", "Barcelona", "Ath.Bilbao", "Real Sociedad", "Betis", "Getafe", "Valencia",
    "Las Palmas", "Rayo Vallecano", "Osasuna", "Villareal", "Mallorca", "Alaves", "Sevilla", "Celta Vigo", "Cadiz",
    "Granada", "Almeria")

equipas_lista = sorted(equipas)

print("-------------------------")
time.sleep(2)

print("Os primeiros 5 qualificados são :")
for e in equipas[0:5]:
    print(f"{e}")

print("-------------------------")
time.sleep(2)
print("Os ultimos 4 qualificados são: ")
for e in equipas[-5:-1]:
    print(e)

print("-------------------------")
time.sleep(2)
print(" Aqui esta a lista total de equipas por ordem alfabetica :")
for e in sorted(equipas):
    print(e)

print("-------------------------")
time.sleep(2)
print(f"Las Palmas encontra-se na posição {equipas.index("Las Palmas") + 1}")
