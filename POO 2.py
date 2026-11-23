class Produto:
    def __init__(self, nome, preço, estoque):
        self.nome = nome
        self.preço = preço
        self.estoque = estoque

    def exibir(self):
                print(f"produto:  {self.nome}")
                print(f"Preço: {self.preço}")
                print(f"Estoque: {self.estoque}")
                print("-" * 80)


p1 = Produto("Arroz", 5.99, 30)
p2 = Produto

p1.exibir()
p2.exibir()