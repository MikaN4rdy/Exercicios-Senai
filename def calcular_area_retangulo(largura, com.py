def calcular_area_retangulo(largura, comprimento):
    area = largura * comprimento
    return area




largura = float(input("Digite a largura do retângulo: "))
comprimento = float(input("Digite o comprimento do retângulo: "))


resultado = calcular_area_retangulo(largura, comprimento)


print(f"A área do retângulo é: {resultado}")