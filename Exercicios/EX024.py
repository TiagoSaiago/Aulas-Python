# Introdução do numero por parte do utilizador
i = int(input("Digite um numero inteiro: "))

total = 0

# Formula de verificação se o numero introduzido é primo ou não

for x in range(1, i + 1):
    if i % x == 0:
        total += 1
if total == 2:
    print(f"O numero {i} é primo, foi divisivel {total} vezes")
else:
    print(f"o numero {i} não é primo, foi divisivel {total} vezes")
