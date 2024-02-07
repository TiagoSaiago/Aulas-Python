velocidade = int(input("Introduza a sua velocidade: "))
multa = (velocidade - 80) * 7 + 100

if velocidade > 80:
    print(f"Multado: {multa}€ ")
else:
    print("Não Multado")
