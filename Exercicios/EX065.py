from time import sleep
import datetime


# Funçoes
def mensagem_bem_vindo(msg):
    """
    --> Uma função que imprime uma mensagem com separadores por cima
    :param msg: mensagem personalizada
    :return: não tem return
    """
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(msg)
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")


def validador_carta(ano):
    """
    --> programa onde checka se a pessoa pode tirar a carta de condução tendo como unico argumento o ano de nascimento
    :param ano: onde se introduz o ano da pessoa
    :return: não possui return
    """
    year = datetime.date.today().year
    idade = year - ano
    print(f"A sua idade é {idade}")
    if idade >= 18:
        print("Pode tirar a carta")
    if idade < 16:
        print("Não pode tirar a carta")
    if 18 > idade >= 16:
        print("Pode  tirar a carta com auturização")


mensagem_bem_vindo("Bem Vindo")
validador_carta(2008)
