def parImpar (numero):
    if numero % 2 == 0:
        return 'Par'
    else:
        return 'Impar'
 
entrada = input('Digite um número inteiro: ')
entradaTexto = input('Digite uma palavra: ')

try:
    numero = int(entrada)
    inteiro = parImpar (numero)   
except:
    print('ERRO') 


def contar_caracteres(texto):
    if texto == texto:
         return len(texto)
    else:
        return len(texto)    

try:
    text = (entradaTexto)
    palavra = contar_caracteres (text)
    print(f"O numero é {inteiro} é a palavra tem {palavra} digitos")    
except:
    print('ERRO') 