# Crie um programa que pede ao usuário para inserir um número 
# inteiro e usa try e except para garantir que a entrada 
# seja realmente um número inteiro.
# Solicitar um número ao usuário

entrada = input("Digite um número inteiro: ")

# Tentar converter a entrada para um número inteiro
try:
    numero = int(entrada)
    print(f"Você digitou o número inteiro: {numero}")
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

