# Crie uma função que conta o número de caracteres em uma string fornecida pelo usuário. 
# Use try e except para garantir que a entrada seja uma string.

def contar_caracteres(texto):
    return len(texto)

# Solicitar uma string ao usuário
entrada = input("Digite uma palavra ou frase: ")

# Tentar chamar a função contar_caracteres
try:
    caracteres = contar_caracteres(entrada)
    print(f"A string '{entrada}' tem {caracteres} caracteres.")
except TypeError:
    print("Erro: Por favor, insira uma string válida.")
