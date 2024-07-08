numero= input("Digite um numero: ")
texto = input("Digite um texto: ")

def imparpar(numero):
        if numero % 2 == 0:
            return "numero par"
        else:
            return "numero impar"

def contar_caracteres (texto):
    return len(texto)

try:
    numero1 = int(numero)
    resultado = imparpar(numero1)
    quantidade = contar_caracteres(texto)
    print(f"O número {numero1} é {resultado}")
    print (f"O texto {texto} possui {quantidade} caracteres.")
except:
    print("Erro: Digite um numero inteiro")
    print('Tem quer ser texto, digite um por favor')
