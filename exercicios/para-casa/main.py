def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"
    
def contar_caracteres(texto):
    return len(texto)

entrada_n = input("Digite um número inteiro: ")
entrada_txt = input("Digite uma palavra ou frase: ")

try:
    numero = int(entrada_n)
    resultado = verificar_par_impar(numero)
    print(f"O número {numero} é {resultado}.")

    caracteres = contar_caracteres(entrada_txt)
    print(f"A string '{entrada_txt}' tem {caracteres} caracteres.")

except:
    print("Erro: Por favor, insira 1uma string válida.")
    print("Erro: Por favor, insira um número inteiro válido.")