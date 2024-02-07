def soma(a, b):
    """
    --> Esta função imprime no ecrã a soma entre as variaveis
    :param a: primeiro numero da soma
    :param b: segundo numero da soma
    :return: sem retorno
    """
    s = a + b
    print(f"A soma entre {a} e {b} é igual a {s}")


soma(10, 15)
print("-" * 10)
help(soma)


def somas(a=0, b=0, c=0):
    """

    :param a:
    :param b:
    :param c:
    :return:
    """
    s = a + b + c
    return s


resultado = somas(c=1, b=2, a=3)
resultado2 = somas(75, 43, 12)
print(f"A primeira soma entre vale {resultado} e a segunda vale {resultado2}")

quit()
