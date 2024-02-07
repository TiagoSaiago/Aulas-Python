import random

import operator

jogadores = {"Tiago": random.randint(1, 6), "Hélder": random.randint(1, 6), "Rui": random.randint(1, 6),
             "João": random.randint(1, 6)}

for jogador in jogadores:
    for x in range(1, 5):
        print(f"Em {x} lugar ficou:")
        print(f"Em {} obteve o numero do dado de {}")
