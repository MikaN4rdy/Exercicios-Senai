class Usuario:
    def __init__(self, nome):
        self.nome= nome
        self.limite = 1
        self.emprestados = []


    def pegar_livro(self, livro):
        if len(self.emprestados) < self.limite:
            livro.emprestar()
            self.emprestados.append(livro)