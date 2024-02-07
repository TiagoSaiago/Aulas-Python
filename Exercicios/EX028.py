# Primeira Pergunta
print("Portugal é um país?.")
print("[V / F] ?")
resp = input("--->").strip().upper()

# loop para ter resposta adequada
while resp not in 'VF':
    print("Por favor digite 'V para verdadeiro e 'F' para Falso")
    resp = input("--->").strip().upper()

# validação resposta 1
if resp in 'F':
    print("Está errado!!")
elif resp in "V":
    print("Está certo!!")

print("Uma centopeia tem 100 patas?")
print("[V / F] ?")
resp = input("--->").strip().upper()

while resp not in 'VF':
    print("Por favor digite 'V para verdadeiro e 'F' para Falso")
    resp = input("--->").strip().upper()

# validação resposta 2
if resp in 'F':
    print("Está errado!!")
elif resp in "V":
    print("Está certo!!")

print("França é um país?")
print("[V / F] ?")
resp = input("--->").strip().upper()

while resp not in 'VF':
    print("Por favor digite 'V para verdadeiro e 'F' para Falso")
    resp = input("--->").strip().upper()

# validação resposta 3
if resp in 'F':
    print("Está errado!!")
elif resp in "V":
    print("Está certo!!")
