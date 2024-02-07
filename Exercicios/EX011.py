# Introdução de dados pelo utilizador
frase = input("Introduza uma frase: ")
# Formatação da frase para maiusculo para facilidade
frase_maiuscula = frase.upper()
letra_a = frase_maiuscula.count("A")
posicao_primeira_a = frase_maiuscula.find("A")
posicao_ultima_a = frase_maiuscula.rfind("A")

print(f"A sua frase contem a letra A {letra_a} vezes")
print(f"aparece pela primeira vez em {posicao_primeira_a + 1}")
print(f"Aparece pela ultima vez em {posicao_ultima_a + 1}")
