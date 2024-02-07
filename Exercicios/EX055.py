jogador = dict()

jogador["Nome"] = input("Digite o nome: ")
jogador["Jogos"] = int(input("Quantos jogos jogou?: "))
jogador["Golos"] = int(input("Quantos golos marcou?: "))
jogador["Média de Golos"] = (jogador["Golos"] / jogador["Jogos"])

print(f"{jogador["Nome"]} teve uma média de {jogador["Média de Golos"]} por jogo")
