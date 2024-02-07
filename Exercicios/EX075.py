class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def descrever(self):
        print(f"O livro {self.titulo} foi escrito por {self.autor}")


livro1 = Livro("Biblia", "JKRowls")
livro2 = Livro("Biblia", "JKRowls")
livro3 = Livro("Biblia", "JKRowls")

print(livro1.titulo + " " + livro1.autor)
print(livro2.titulo + " " + livro2.autor)
print(livro3.titulo + " " + livro3.autor)
print(Livro.descrever(livro2))
