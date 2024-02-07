def pesquisa(a):
    for livro in biblioteca:
        livro["Título"] = livro["Título"].title()
        livro["Autor"] = livro["Autor"].title()
    for livro in biblioteca:
        if a in livro.values():
            print(*(f'{k}: {v}' for k, v in livro.items()), sep='\n', end='\n\n')
            break
    else:
        print(f"Nenhum livro encontrado com o titulo: {a}")


def listagem(a=""):
    for livro in biblioteca:
        print(*(f'{k}: {v}' for k, v in livro.items()), sep='\n', end='\n\n')


biblioteca = [
    {"Título": 'A Casa de Papel', "Autor": 'FOX', "ISBN": '12547', "Ano de Publicação": '2004', "Editora": 'FOX',
     "Categoria ou Gênero": 'AÇÃO', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém',
     "Data de Devolução": None},
    {"Título": 'A CASA', "Autor": 'ACER', "ISBN": '14785', "Ano de Publicação": '1994', "Editora": 'ACER',
     "Categoria ou Gênero": 'DRAMA', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém',
     "Data de Devolução": None},
    {"Título": 'LISBOA LINDA', "Autor": 'GIGA', "ISBN": '5247', "Ano de Publicação": '1995', "Editora": 'FOXX1',
     "Categoria ou Gênero": 'COMEDIA', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém',
     "Data de Devolução": None},
    {"Título": 'O LOBO MAL', "Autor": 'LOUÇA', "ISBN": '9852', "Ano de Publicação": '2004', "Editora": 'FOX',
     "Categoria ou Gênero": 'AÇÃO', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém',
     "Data de Devolução": None},
    {"Título": 'SURFISTINHA', "Autor": 'ACER', "ISBN": '9854', "Ano de Publicação": '1994', "Editora": 'ACER',
     "Categoria ou Gênero": 'DRAMA', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém',
     "Data de Devolução": None},
    {"Título": 'O PINTO DA COSTA', "Autor": 'FOXX1', "ISBN": '1025', "Ano de Publicação": '1995',
     "Editora": 'FOXX1',
     "Categoria ou Gênero": 'COMEDIA', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém',
     "Data de Devolução": None},
    {"Título": 'O PORTO', "Autor": 'FOX', "ISBN": '12547', "Ano de Publicação": '2004', "Editora": 'FOX',
     "Categoria ou Gênero": 'AÇÃO', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém',
     "Data de Devolução": None},
    {"Título": 'LIMBO FEROZ', "Autor": 'LONG', "ISBN": '14785', "Ano de Publicação": '1994', "Editora": 'ACER',
     "Categoria ou Gênero": 'DRAMA', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém',
     "Data de Devolução": None},
    {"Título": 'PYTHON', "Autor": 'FOX2', "ISBN": '85214', "Ano de Publicação": '1995', "Editora": 'FOXX1',
     "Categoria ou Gênero": 'COMEDIA', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém',
     "Data de Devolução": None},
    {"Título": 'JAVA', "Autor": 'GIGA', "ISBN": '12547', "Ano de Publicação": '2004', "Editora": 'FOX',
     "Categoria ou Gênero": 'AÇÃO', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém',
     "Data de Devolução": None},
    {"Título": 'LIVRO DE COZINHA', "Autor": 'PIA', "ISBN": '14785', "Ano de Publicação": '1994', "Editora": 'ACER',
     "Categoria ou Gênero": 'DRAMA', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém',
     "Data de Devolução": None},
    {"Título": 'CULINARIA AFRICANA', "Autor": 'KIA', "ISBN": '85236', "Ano de Publicação": '1995',
     "Editora": 'FOXX1',
     "Categoria ou Gênero": 'COMEDIA', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém',
     "Data de Devolução": None},
    {"Título": 'O VERÃO PASSADO', "Autor": 'KA', "ISBN": '125477', "Ano de Publicação": '2004', "Editora": 'FOX',
     "Categoria ou Gênero": 'AÇÃO', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém',
     "Data de Devolução": None},
    {"Título": 'EFEITOS DE DIREITO', "Autor": 'ACER', "ISBN": '1478547', "Ano de Publicação": '1994',
     "Editora": 'ACER',
     "Categoria ou Gênero": 'DRAMA', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém',
     "Data de Devolução": None},
    {"Título": 'O ADVOGADO', "Autor": 'FOX', "ISBN": '1025417', "Ano de Publicação": '1995', "Editora": 'FOXX1',
     "Categoria ou Gênero": 'COMEDIA', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém',
     "Data de Devolução": None}]

while True:
    print("[ 1 ] - Adicionar Livro")
    print("[ 2 ] - Remover Livro")
    print("[ 3 ] - Listar Livros")
    print("[ 4 ] - Procurar Livro")
    print("[ 5 ] - Emprestar Livro")
    print("[ 6 ] - Devolver Livro")
    print("[ 0 ] - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        pass
    elif opcao == "2":
        pass
    elif opcao == "3":
        listagem()
    elif opcao == "4":
        pesquisar = input("Pesquise o Livro por Titulo, Autor ou ISBN: ").title()
        pesquisa(pesquisar)
    elif opcao == "5":
        pass
    elif opcao == "6":
        pass
    elif opcao == "0":
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
