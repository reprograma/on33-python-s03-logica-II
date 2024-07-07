def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

def contar_caracteres(texto):
    return len(texto)

numero_input = input("Insira um número: ")
texto_input = input("Insira um texto: ")

try:

    numero = int(numero_input)
    
    resultado_paridade = verificar_par_ou_impar(numero)
    print(f"O número {numero} é {resultado_paridade}.")
    
    quantidade_caracteres = contar_caracteres(texto_input)
    print(f"O texto inserido tem {quantidade_caracteres} caracteres.")

except ValueError:
    print("Entrada inválida. Por favor, insira um número válido.")