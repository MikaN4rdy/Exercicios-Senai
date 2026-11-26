
# Classe responsável por criar os livros
class Livro:
    # Inicializa os atributos do livro
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponivel = "Sim"

    # Exibe as informações do livro
    def descricao(self):
        print("\n--- Descrição do Livro ---")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Páginas: {self.paginas}")
        print(f"Disponível: {self.disponivel}")

    # Verifica se o livro está disponível e realiza o empréstimo
    def emprestar(self):
        if self.disponivel == "Sim":
            self.disponivel = "Não"
            print("Livro emprestado com sucesso!")
            return True
        else:
            print("Livro não está disponível.")
            return False

    # Altera a disponibilidade do livro para Sim
    def devolver(self):
        if self.disponivel == "Não":
            self.disponivel = "Sim"
            print("Livro devolvido com sucesso!")
        else:
            print("O livro já está disponível.")


# Lista de livros cadastrados
livro1 = Livro("Black Clover", "Yuki Tabata", 192)
livro2 = Livro("Jujutsu Kaisen", "Mariana Oliveira", 192)
livro3 = Livro("Death Note", "Tsugumi", 192)
livro4 = Livro("Bungou Stray Dogs", "Kafka Asagiri", 196)

livros = [livro1, livro2, livro3, livro4]


# Classe responsável por criar os usuários
class Usuario:
    # Inicializa o nome, limite e lista de livros emprestados
    def __init__(self, nome):
        self.nome = nome
        self.limite = 1
        self.emprestados = []

    # Realiza o empréstimo respeitando o limite do usuário
    def pegar_livro(self, livro):
        if len(self.emprestados) >= self.limite:
            print(f"{self.nome} atingiu o limite de {self.limite} livros!")
            return

        if livro.emprestar():
            self.emprestados.append(livro)

    # Verifica se o livro pertence ao usuário e realiza a devolução
    def devolver_livro(self, livro):
        if livro in self.emprestados:
            livro.devolver()
            self.emprestados.remove(livro)
        else:
            print("Este livro não pertence aos seus empréstimos.")


# Classe Aluno que herda os atributos e métodos de Usuario
class Aluno(Usuario):
    # Inicializa o aluno e define seu limite de empréstimos
    def __init__(self, nome):
        super().__init__(nome)
        self.limite = 2


# Classe Professor que herda os atributos e métodos de Usuario
class Professor(Usuario):
    # Inicializa o professor e define seu limite de empréstimos
    def __init__(self, nome):
        super().__init__(nome)
        self.limite = 5


# Lista que armazena os usuários cadastrados
usuarios = []


# MENU PRINCIPAL
# Mantém o programa funcionando até o usuário escolher sair
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
    # Percorre a lista e exibe a descrição de cada livro
    if opcao == "1":
        for i, livro in enumerate(livros):
            print(f"\nLivro {i + 1}")
            livro.descricao()

    # CADASTRAR ALUNO
    # Solicita o nome e adiciona um novo aluno à lista
    elif opcao == "2":
        nome = input("Digite o nome do aluno: ")

        aluno = Aluno(nome)
        usuarios.append(aluno)

        print(f"Aluno {nome} cadastrado!")
        print(f"Limite de empréstimos: {aluno.limite}")

    # CADASTRAR PROFESSOR
    # Solicita o nome e adiciona um novo professor à lista
    elif opcao == "3":
        nome = input("Digite o nome do professor: ")

        professor = Professor(nome)
        usuarios.append(professor)

        print(f"Professor {nome} cadastrado!")
        print(f"Limite de empréstimos: {professor.limite}")

    # EMPRESTAR LIVRO
    # Permite escolher um usuário e um livro para realizar o empréstimo
    elif opcao == "4":

        # Verifica se existem usuários cadastrados
        if not usuarios:
            print("Cadastre um usuário primeiro!")
            continue

        print("\n--- USUÁRIOS CADASTRADOS ---")

        # Exibe todos os usuários cadastrados
        for i, usuario in enumerate(usuarios):
            print(f"{i + 1} - {usuario.nome} | Limite: {usuario.limite}")

        escolha_usuario = int(input("Escolha o usuário: "))

        # Verifica se o número do usuário é válido
        if 1 <= escolha_usuario <= len(usuarios):
            usuario = usuarios[escolha_usuario - 1]

            print("\n--- ESCOLHA UM LIVRO ---")

            # Exibe todos os livros disponíveis na lista
            for i, livro in enumerate(livros):
                print(f"{i + 1} - {livro.titulo} | Disponível: {livro.disponivel}")

            escolha = int(input("Digite o número do livro: "))

            # Verifica se o número do livro é válido
            if 1 <= escolha <= len(livros):
                livro = livros[escolha - 1]
                usuario.pegar_livro(livro)
            else:
                print("Livro não encontrado!")
        else:
            print("Usuário não encontrado!")

    # DEVOLVER LIVRO
    # Permite escolher um usuário e devolver um livro emprestado
    elif opcao == "5":

        # Verifica se existem usuários cadastrados
        if not usuarios:
            print("Não existem usuários cadastrados!")
            continue

        print("\n--- USUÁRIOS CADASTRADOS ---")

        # Exibe os usuários para selecionar quem fará a devolução
        for i, usuario in enumerate(usuarios):
            print(f"{i + 1} - {usuario.nome}")

        escolha_usuario = int(input("Escolha o usuário: "))

        # Verifica se o número do usuário é válido
        if 1 <= escolha_usuario <= len(usuarios):
            usuario = usuarios[escolha_usuario - 1]

            # Verifica se o usuário possui livros emprestados
            if not usuario.emprestados:
                print("Este usuário não possui livros emprestados!")
                continue

            print("\n--- LIVROS EMPRESTADOS ---")

            # Exibe os livros que pertencem aos empréstimos do usuário
            for i, livro in enumerate(usuario.emprestados):
                print(f"{i + 1} - {livro.titulo}")

            escolha = int(input("Digite o número do livro: "))

            # Verifica se o número do livro é válido
            if 1 <= escolha <= len(usuario.emprestados):
                livro = usuario.emprestados[escolha - 1]
                usuario.devolver_livro(livro)
            else:
                print("Livro não encontrado!")
        else:
            print("Usuário não encontrado!")

    # VER USUÁRIOS
    # Exibe as informações de todos os usuários cadastrados
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
    # Encerra a repetição e finaliza o programa
    elif opcao == "7":
        print("Obrigado por utilizar o programa!")
        break

    # Informa quando o usuário digita uma opção inválida
    else:
        print("Opção inválida!")
