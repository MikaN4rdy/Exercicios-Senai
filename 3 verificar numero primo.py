def verificar_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
def listar_primos():
    primos = []
    for numero in range(1, 101):
        if verificar_primo(numero):
            primos.append(numero)
    return primos
numero = int(input("Digite um número inteiro: "))
if verificar_primo(numero):
    print(f"O número {numero} é primo!")
else:
    print(f"O número {numero} não é primo.")
    print("Lista de números primos de 1 a 100:")
    print(listar_primos())