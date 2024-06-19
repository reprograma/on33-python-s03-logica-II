def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "número par"
    else:
        return "número ímpar"
    
parImpar = input('Digite um número: ')

try:
    numero = int(parImpar)
    resultado = verificar_par_impar(numero)
except:
    print('Erro. Atenção! Digite um número inteiro.')

def contar_caracteres(texto):
    return len(texto)

palavra1 = input('Digite uma palavra: ')

try:
    caracteres = contar_caracteres(palavra1)
    print(f"O {parImpar} é {resultado}, e a palavra {palavra1} tem {caracteres} caracteres. ")
except:
    print('Digite uma palavra válida!')

