# Crie um programa que classifica a idade de uma pessoa em categorias (criança, adolescente, adulto, idoso).
# Solicitar a idade ao usuário
entrada_idade = input("Digite a sua idade: ")

# Verificar se a entrada é um número inteiro
if entrada_idade.isdigit():
    idade = int(entrada_idade)
    
    # Classificar a idade
    if idade < 0:
        print("Idade inválida. Por favor, insira um número não negativo.")
    elif idade <= 12:
        print("Você é uma criança.")
    elif idade <= 17:
        print("Você é um adolescente.")
    elif idade <= 64:
        print("Você é um adulto.")
    else:
        print("Você é um idoso.")
else:
    print("Erro: Por favor, insira um número inteiro válido.")

