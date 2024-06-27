def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

def contar_caracteres(texto):
    return len(texto)

try:
    numero = int(input("Digite um número: "))
    texto = input("Insira um texto: ")
    
    # Verificar se o número é par ou ímpar
    resultado_par_impar = verificar_par_impar(numero)
    print(f"O número {numero} é {resultado_par_impar}.")
    
    # Contar os caracteres do texto
    quantidade_caracteres = contar_caracteres(texto)
    print(f"O texto tem {quantidade_caracteres} caracteres.")
    
except ValueError:
    print("Entrada inválida! Insira um número válido.")
