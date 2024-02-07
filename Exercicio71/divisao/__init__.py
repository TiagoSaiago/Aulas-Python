

def divisao(a,b):
    x = a / b
    return x


try:
    divisao(30, 5)

except Exception as erro:
    print(f"ERRO! --- {erro}")

else:
    print(f"Sucesso!")
