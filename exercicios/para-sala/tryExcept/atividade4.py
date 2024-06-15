# Crie um programa que pede ao usuário para inserir 
# uma temperatura em graus Celsius e converte para Fahrenheit. 
# Use try e except para garantir que a entrada seja um número.

# Solicitar uma temperatura em graus Celsius ao usuário
entrada = input("Digite a temperatura em graus Celsius: ")

# Tentar converter a entrada para um número
try:
    celsius = float(entrada)
    fahrenheit = celsius * 9/5 + 32
    print(f"A temperatura em Fahrenheit é: {fahrenheit}")
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número.")
