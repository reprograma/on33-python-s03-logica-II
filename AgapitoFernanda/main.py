entradaNum = input("digite um numero: ")

entrada = input("Digite uma palavra ou frase: ")

def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"
    
try:
    numero = int(entradaNum)
    resultado = verificar_par_impar(numero)
    print(f"O número {numero} é {resultado}.")
except ValueError:
    print("Erro: Por favor, insira um número inteiro válido.")



def contar_caracteres(texto):
    return len(texto)

try:
    caracteres = contar_caracteres(entrada)
    if entrada.isalpha() == False:
        print('Digite apenas letras.')
    else:
        print(f"A palavra '{entrada}' tem {caracteres} caracteres.")
except TypeError:
    print("Erro: Por favor, insira uma string válida.")


