# Crie uma função que converte uma temperatura de graus Celsius para Fahrenheit. 
# Use try e except para garantir que a entrada seja um número.

def celsius_para_fahrenheit(celsius):
    return celsius * 9/5 + 32

# Solicitar uma temperatura em graus Celsius ao usuário
entrada = input("Digite a temperatura em graus Celsius: ")

# Tentar converter a entrada para um número e chamar a função celsius_para_fahrenheit
try:
    celsius = float(entrada)
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f"A temperatura em Fahrenheit é: {fahrenheit}")
except ValueError:
    print("Erro: Por favor, insira um número válido.")
