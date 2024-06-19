def verificar_par_impar(numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'impar'

def contar_caracteres(texto):
    return len(texto)

entrada_numero = input('Digite um número inteiro: ')
texto = input('Digite um texto: ')

try:
    numero = int(entrada1)
    resultado = par_impar(numero)
    print(f"O número {numero} é {resultado}.")

    caracteres = contar_caracteres(entrada_txt)
    print(f"A string '{entrada_txt}' tem {caracteres} caracteres.")   


except:
    print('ERRO') 