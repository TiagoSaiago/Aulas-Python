def so_nums(a):
    if a.isdigit():
        print(a)
    else:
        print("Não inseriu um numero")


resposta = input("Insira um numero: ")
so_nums(resposta)
