import random
import time

# Variavel que guarda um número random de 0 a 7
numeros = random.randint(0, 7)

# Escolha do número pela parte do utilizador
numeroEscolhido = int(input('Estou a pensar num numero de 0 a 7 consegues adivinhar?  '))

print("Hmm....")
time.sleep(2)
print("....")
time.sleep(2)

# Condição para verificar se o utilizador escolheu o número certo
if numeroEscolhido == numeros:
    print(f"Acertaste! o numero que eu pensei era {numeros}")
else:
    print(f"Perdeste :( , eu escolhi {numeros} e tu disseste {numeroEscolhido}")
