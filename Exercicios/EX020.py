import random

playerPick = input("Escolha entre Pedra, Papel ou Tesoura: ").upper()
lista = ["PEDRA", "PAPEL", "TESOURA"]
pcPick = random.choice(lista)

if playerPick == "PEDRA" and pcPick == "PAPEL":
    print(f"Perdeste, eu escolhi {pcPick} e tu escolheste {playerPick}")
elif playerPick == "PEDRA" and pcPick == "TESOURA":
    print(f"Ganhaste, eu escolhi {pcPick} e tu escolheste {playerPick}")
elif playerPick == pcPick:
    print("Empate!")
elif playerPick == "TESOURA" and pcPick == "PEDRA":
    print(f"Perdeste, eu escolhi {pcPick} e tu escolheste {playerPick}")
elif playerPick == "TESOURA" and pcPick == "PAPEL":
    print(f"Ganhaste, eu escolhi {pcPick} e tu escolheste {playerPick}")
elif playerPick == "PAPEL" and pcPick == "TESOURA":
    print(f"Perdeste, eu escolhi {pcPick} e tu escolheste {playerPick}")
elif playerPick == "PAPEL" and pcPick == "PEDRA":
    print(f"Ganhaste, eu escolhi {pcPick} e tu escolheste {playerPick}")
elif playerPick == "TESOURA" and pcPick == "PEDRA":
    print(f"Perdeste, eu escolhi {pcPick} e tu escolheste {playerPick}")
