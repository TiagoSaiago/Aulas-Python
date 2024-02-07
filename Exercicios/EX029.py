import random

cpu_pick = random.randint(1, 10)
tentativas = 1

print("Consegues adivinhar em que numero estou a pensar entre 1 e 10?")
resposta_utilizador = int(input("--->"))

while resposta_utilizador != cpu_pick:
    if resposta_utilizador > cpu_pick:
        print("errado! mais baixo, tenta mais uma vez")
        tentativas += 1
        resposta_utilizador = int(input("--->"))
    elif resposta_utilizador < cpu_pick:
        print("errado! mais alto, tenta mais uma vez")
        tentativas += 1
        resposta_utilizador = int(input("--->"))

print(f"Acertaste , tentaste {tentativas} vezes mas chegaste lá")
