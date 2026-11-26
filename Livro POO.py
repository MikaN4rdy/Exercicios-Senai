class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponivel = "Sim"

    def descricao(self):
        print("\n--- Descrição do Livro ---")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Páginas: {self.paginas}")
        print(f"Disponível: {self.disponivel}")

    def emprestar(self):
        if self.disponivel == "Sim":
            self.disponivel = "Não"
            print("Livro emprestado com sucesso!")
            return True
        else:
            print("Livro não está disponível.")
            return False

    def devolver(self):
        if self.disponivel == "Não":
            self.disponivel = "Sim"
            print("Livro devolvido com sucesso!")
        else:
            print("O livro já está disponível.")


# Lista de livros
livro1 = Livro("Black Clover", "Yuki Tabata", 192)
livro2 = Livro("Jujutsu Kaisen", "Mariana Oliveira", 192)
livro3 = Livro("Bleach", "Tite Kubo", 192)
livro4 = Livro("Bungou Stray Dogs", "Kafka Asagiri", 196)

livros = [livro1, livro2, livro3, livro4]


# Classe Usuario
class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.limite = 1
        self.emprestados = []

    def pegar_livro(self, livro):
        if len(self.emprestados) >= self.limite:
            print(f"{self.nome} atingiu o limite de {self.limite} livros!")
            return

        if livro.emprestar():
            self.emprestados.append(livro)

    def devolver_livro(self, livro):
        if livro in self.emprestados:
            livro.devolver()
            self.emprestados.remove(livro)
        else:
            print("Este livro não pertence aos seus empréstimos.")


# Classe Aluno
class Aluno(Usuario):
    def __init__(self, nome):
        super().__init__(nome)
        self.limite = 2


# Classe Professor
class Professor(Usuario):
    def __init__(self, nome):
        super().__init__(nome)
        self.limite = 5


# Lista de usuários
usuarios = []


# MENU PRINCIPAL
while True:
    print("\n**** SISTEMA DE BIBLIOTECA ****")
    print("1 - Ver livros")
    print("2 - Cadastrar aluno")
    print("3 - Cadastrar professor")
    print("4 - Emprestar livro")
    print("5 - Devolver livro")
    print("6 - Ver usuários")
    print("7 - Sair")

    opcao = input("\nEscolha uma opção: ")

    # VER LIVROS
    if opcao == "1":
        for i, livro in enumerate(livros):
            print(f"\nLivro {i + 1}")
            livro.descricao()

    # CADASTRAR ALUNO
    elif opcao == "2":
        nome = input("Digite o nome do aluno: ")

        aluno = Aluno(nome)
        usuarios.append(aluno)

        print(f"Aluno {nome} cadastrado!")
        print(f"Limite de empréstimos: {aluno.limite}")

    # CADASTRAR PROFESSOR
    elif opcao == "3":
        nome = input("Digite o nome do professor: ")

        professor = Professor(nome)
        usuarios.append(professor)

        print(f"Professor {nome} cadastrado!")
        print(f"Limite de empréstimos: {professor.limite}")

    # EMPRESTAR LIVRO
    elif opcao == "4":

        if not usuarios:
            print("Cadastre um usuário primeiro!")
            continue

        print("\n--- USUÁRIOS CADASTRADOS ---")

        for i, usuario in enumerate(usuarios):
            print(f"{i + 1} - {usuario.nome} | Limite: {usuario.limite}")

        escolha_usuario = int(input("Escolha o usuário: "))

        if 1 <= escolha_usuario <= len(usuarios):
            usuario = usuarios[escolha_usuario - 1]

            print("\n--- ESCOLHA UM LIVRO ---")

            for i, livro in enumerate(livros):
                print(f"{i + 1} - {livro.titulo} | Disponível: {livro.disponivel}")

            escolha = int(input("Digite o número do livro: "))

            if 1 <= escolha <= len(livros):
                livro = livros[escolha - 1]
                usuario.pegar_livro(livro)
            else:
                print("Livro não encontrado!")
        else:
            print("Usuário não encontrado!")

    # DEVOLVER LIVRO
    elif opcao == "5":

        if not usuarios:
            print("Não existem usuários cadastrados!")
            continue

        print("\n--- USUÁRIOS CADASTRADOS ---")

        for i, usuario in enumerate(usuarios):
            print(f"{i + 1} - {usuario.nome}")

        escolha_usuario = int(input("Escolha o usuário: "))

        if 1 <= escolha_usuario <= len(usuarios):
            usuario = usuarios[escolha_usuario - 1]

            if not usuario.emprestados:
                print("Este usuário não possui livros emprestados!")
                continue

            print("\n--- LIVROS EMPRESTADOS ---")

            for i, livro in enumerate(usuario.emprestados):
                print(f"{i + 1} - {livro.titulo}")

            escolha = int(input("Digite o número do livro: "))

            if 1 <= escolha <= len(usuario.emprestados):
                livro = usuario.emprestados[escolha - 1]
                usuario.devolver_livro(livro)
            else:
                print("Livro não encontrado!")
        else:
            print("Usuário não encontrado!")

    # VER USUÁRIOS
    elif opcao == "6":
        if not usuarios:
            print("Nenhum usuário cadastrado!")
        else:
            for usuario in usuarios:
                print(f"\nNome: {usuario.nome}")
                print(f"Tipo: {type(usuario).__name__}")
                print(f"Limite: {usuario.limite}")
                print(f"Livros emprestados: {len(usuario.emprestados)}")

    # SAIR
    elif opcao == "7":
        print("Obrigado por utilizar o programa!")
        break

    else:
        print("Opção inválida!")