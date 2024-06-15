# Crie um programa que pede ao usuário para inserir um número inteiro 
# e verifica se o número é par ou ímpar. 
# Use try e except para garantir que a entrada seja um número inteiro.

# Solicitar um número ao usuário
entrada = input("Digite um número inteiro: ")

# Tentar converter a entrada para um número inteiro
try:
    numero = int(entrada)
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
