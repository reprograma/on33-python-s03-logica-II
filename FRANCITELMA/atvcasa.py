def verificar_par_impar(numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'impar'
    
entrada = input("Por favor, digite um número inteiro: ")

try:
    numero = int(entrada)
    resultado = verificar_par_impar(numero)
    print(f"O número {numero} que você digitou é {resultado}")
except:
    print("Erro: Esse número não é um número inteiro!")

def contar_caracteres(texto):
    return len(texto)
entrada = input('Agora digite uma palavra ou uma frase: ')
try:
    caracteres = contar_caracteres(entrada)
    print(f'A string {entrada}, tem {caracteres} caracteres')
except:
    print('Erro, digite uma palavra ou frase!')

#

def parImpar(caracteres):
    if caracteres % 2 == 0:
        return 'par'
    else:
        return 'impar'   
    
try:
    numero = int(caracteres)
    resultado = parImpar(numero)
    print(f"E o número {numero} é {resultado}")
except:
    print("Erro: Esse número não é um número inteiro!")