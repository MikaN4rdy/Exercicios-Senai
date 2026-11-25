
class Produto:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True

    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
            print("Produto emprestado!")
        else:
            print("produto indisponível!")

    def devolver(self):
        self.disponivel = True
        print("produto devolvido!")

    def descricao(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"Disponível: {self.disponivel}")


class Usuario:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.livros_emprestados = []

    def pegar_livro(self, livro):
        if livro.disponivel == True:
            livro.emprestar()
            self.livros_emprestados.append(livro)
        else:
            print("Produto indisponível!")


class Aluno(Usuario):
    def pegar_livro(self, livro):
        if len(self.livros_emprestados) < 2:
            if livro.disponivel == True:
                livro.emprestar()
                self.livros_emprestados.append(livro)
            else:
                print("Produto indisponível!")
        else:
            print("Aluno pode pegar no máximo 2 livros!")


class Professor(Usuario):
    def pegar_livro(self, livro):
        if len(self.livros_emprestados) < 5:
            if livro.disponivel == True:
                livro.emprestar()
                self.livros_emprestados.append(livro)
            else:
                print("Livro indisponível!")
        else:
            print("Professor pode pegar no máximo 5 livros!")


# Criando livros
livro1 = Livro("Dom Casmurro", "Machado de Assis", "12345")
livro2 = Livro("Harry Potter", "J.K. Rowling", "67890")
livro3 = Livro("O Hobbit", "J.R.R. Tolkien", "11223")

# Criando usuários
aluno1 = Aluno("Carlos", "001")
professor1 = Professor("Ana", "002")

# Realizando empréstimos
aluno1.pegar_livro(livro1)
aluno1.pegar_livro(livro2)

professor1.pegar_livro(livro3)

# Exibindo descrição
livro1.descricao()

# Devolvendo livro
livro1.devolver()
