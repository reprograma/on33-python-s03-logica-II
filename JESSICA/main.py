# ESSE PROGRAMA TEM COMO OBJETIVOS
# 1. Verificar se um número fornecido pelo usuário é par ou ímpar.
#2. Contar os caracteres de um texto fornecido pelo usuário

def verificar_par_impar (numero):
    if numero % 2 == 0:
        return "é um número par!🐥🐥"
    else:
        return "é um número ímpar!🐥"

def contar_caracteres (texto):
    return len(texto)

entrada_numero = input("Digite um número inteiro: ")
entrada_texto = input("Digite um texto ou uma frase: ")

try:
    numero = int(entrada_numero)
    resultado_numero = verificar_par_impar(numero)
    resultado_texto = contar_caracteres(entrada_texto)
    print(f"\nAQUI ESTÁ SEU RESULTADO:\n{numero} {resultado_numero} \nO texto ::: {entrada_texto} ::: tem {resultado_texto} caracteres!!!🎯")

except:
    print("ERRO: por favor, siga as instruções e insira valores válidos")