
class Livro:
    def __init__(self, titulo, autor, isbn, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
            print("Livro emprestado!")
        else:
            print("Livro indisponível!")

    def devolver(self):
        self.disponivel = True
        print("Livro devolvido!")

    def descricao(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"Disponível: {self.disponivel}")


class Usuario:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.limite = 1
        self.livros_emprestados = []

    def pegar_livro(self, livro):
        if len(self.livros_emprestados) < self.limite:
            if livro.disponivel == True:
                livro.emprestar()
                self.livros_emprestados.append(livro)
            else:
                print("Livro indisponível!")
        else:
            print("Limite de livros atingido!")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            livro.devolver()
            self.livros_emprestados.remove(livro)
        else:
            print("Você não possui esse livro!")


class Aluno(Usuario):
    def __init__(self, nome, matricula):
        super().__init__(nome, matricula)
        self.limite = 2

    def pegar_livro(self, livro):
        super().pegar_livro(livro)


class Professor(Usuario):
    def __init__(self, nome, matricula):
        super().__init__(nome, matricula)
        self.limite = 5

    def pegar_livro(self, livro):
        super().pegar_livro(livro)


# Criando livros
livro1 = Livro("Kimetsu no Yaiba", "Koyoharu", "28295")
livro2 = Livro("Jujutsu Kaisen", "Mariana Oliveira", "67890")
livro3 = Livro("Death Note", "Lawliet", "11223")

# Criando usuários
aluno1 = Aluno("Guilherme", "001")
professor1 = Professor("Ana", "002")

# Realizando empréstimos
aluno1.pegar_livro(livro1)
aluno1.pegar_livro(livro2)

professor1.pegar_livro(livro3)

# Exibindo descrição
livro1.descricao()

# Devolvendo livro
aluno1.devolver_livro(livro1)