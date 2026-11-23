class Carros:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir(self):
            print(f"marca: {self.marca}")
            print(f"modelo: {self.modelo}")
            print(f"ano:  {self.ano}")
            print("-" * 80)

p1= Carros("Volvo","XC60 Hibrido", 2008 )
p2= Carros("BMW", "X6", 2022)

p1.exibir()
p2.exibir()