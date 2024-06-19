def verificar_par_impar (numero):
    if numero %2 == 0:
        return "PAR"
    else:
        return "IMPAR"

entrada = input("Insira um número inteiro: ")


def contar_caracteres(texto):
    return len (texto)
    
entrada1 = input("Insira um texto:")

try:
    numero = int(entrada)
    resultado = verificar_par_impar (numero)
    print(f"O número {numero} é {resultado}")
    
    caracteres = contar_caracteres(entrada1)
    print(f"O texto {entrada1}, possui {caracteres} caracteres ")


except:
    print("Digite um número inteiro")