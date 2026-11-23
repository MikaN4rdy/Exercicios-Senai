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
        else:
            print("Livro não está disponível.")


    def devolver(self):
        if self.disponivel == "Não":
            self.disponivel = "Sim"
            print("Livro devolvido com sucesso!")
        else:
            print("O livro já está disponível.")


livro1 = Livro("Kimetsu no Yaiba", "Koyoharu Gotouge", 192)
livro2 = Livro("Jujutsu Kaisen", "Gege Akutami", 192)
livro3 = Livro("Death Note", "Tsugumi Ohba", 192)
livro4 = Livro("Tokyo Ghoul", "Sui Ishida", 196)


livros = [livro1, livro2, livro3, livro4]


while True:
    print("\n===== BIBLIOTECA DE MANGÁS =====")
    print("1 - Ver livros")
    print("2 - Emprestar livro")
    print("3 - Devolver livro")
    print("4 - Sair")


    opcao = input("\nEscolha uma opção: ")


    if opcao == "1":
        for i, livro in enumerate(livros):
            print(f"\nLivro {i + 1}")
            livro.descricao()
    elif opcao == "2":
        print("\n--- ESCOLHA UM MANGÁ ---")


        for i, livro in enumerate(livros):
            print(f"{i + 1} - {livro.titulo} | Disponível: {livro.disponivel}")




        escolha = int(input("\nDigite o número do livro: "))


        if 1 <= escolha <= 4:
            livros[escolha - 1].emprestar()
        else:
            print("Livro não encontrado!")
    elif opcao == "3":
        print("\n--- DEVOLVER MANGÁ ---")


        for i, livro in enumerate(livros):
            print(f"{i + 1} - {livro.titulo} | Disponível: {livro.disponivel}")


        escolha = int(input("\nDigite o número do livro: "))


        if 1 <= escolha <= 4:
            livros[escolha - 1].devolver()
        else:
            print("Livro não encontrado!")
    elif opcao == "4":
        print("Obrigado por utilizar o programa!")
        break
    else:
        print("Opção inválida!")