from time import sleep


def mensagem_bem_vindo(msg):
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(msg)
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")


def interactive_help(a=""):
    mensagem_bem_vindo("Bem vindo ao Interactive Help")
    while a != "fim":
        a = input("Por favor escreva a Função que prefere analisar, se preferir sair escreva 'fim': ").lower()
        sleep(1)
        help(a)
    sleep(1)
    print("Obrigado e espere que volte a utilizar as nossas funcionalidades!")
    sleep(1)
    quit()


interactive_help()
