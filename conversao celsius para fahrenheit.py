def celsius_para_fahrenheit(celsius):
    return (celsius * 1.8) + 32

temp_c = float(input("Digite a temperatura em °C: "))
temp_f = celsius_para_fahrenheit(temp_c)
print(f"{temp_c}°C equivale a {temp_f:.1f}°F")