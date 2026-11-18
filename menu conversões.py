while True:
    print("\n--- MENU DE OPÇÕES ---")
    print("1. Mostrar uma mensagem")
    print("2. Mostrar um cálculo")
    print("3. Sair")
    
    opcao = input("Escolha uma opção (1-3): ")


    if opcao == "1":
        print("\nOlá! Esta é a sua mensagem personalizada.")
    elif opcao == "2":
        resultado = 5 * 4
        print(f"\nCálculo executado: 5 x 4 = {resultado}")
    elif opcao == "3":
        print("\nSaindo do programa... Até logo!")
        break
    else:
        print("\nOpção inválida! Por favor, escolha 1, 2 ou 3")

def celsius_para_fahrenheit(celsius):
    return (celsius * 1.8) + 32

temp_c = float(input("Digite a temperatura em °C: "))
temp_f = celsius_para_fahrenheit(temp_c)
print(f"{temp_c}°C equivale a {temp_f:.1f}°F")