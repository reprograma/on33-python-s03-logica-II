# Crie uma função que verifica se um número é par ou ímpar. 
# Use try e except para garantir que a entrada seja um número.

def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

# Solicitar um número ao usuário
entrada = input("Digite um número inteiro: ")

# Tentar converter a entrada para um número e chamar a função verificar_par_impar
try:
    numero = int(entrada)
    resultado = verificar_par_impar(numero)
    print(f"O número {numero} é {resultado}.")
except ValueError:
    print("Erro: Por favor, insira um número inteiro válido.")
