NotaMatematica = float(input("Digite a Sua nota a Matematica: "))

NotaIngles = float(input("Digite a Sua nota a Ingles: "))

NotaPortugues = float(input("Digite a Sua nota a Portuges: "))

NotaHistoria = float(input("Digite a Sua nota a História: "))

NotaFrances = float(input("Digite a Sua nota a Frances: "))

media = (NotaFrances + NotaHistoria + NotaPortugues + NotaMatematica + NotaIngles) / 5

print(f"Matematica: {NotaMatematica}")
print(f"Ingles: {NotaIngles}")
print(f"Portugues: {NotaPortugues}")
print(f"História: {NotaHistoria}")
print(f"Frances: {NotaFrances}")
print("============================================")
if media >= 9.5:
    print(f"Parabens! Passaste a tua média é {media}")
elif media < 8:
    print(f"A tua media é {media} infelizmente reprovaste, boa sorte para o ano!")
else:
    print(f"A sua média é {media}, está em recuperação")
