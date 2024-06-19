def parImpar(numero):
    if numero % 2 == 0:
        return 'Par'
    else:
        return 'Impar'
        
entradanumero = input("Digite um numero inteiro: ")

def contarCaracteres(texto):
    return len(texto)

entradatexto = input("Digite uma palavra ou uma frase: ")

try:
    numero = int(entradanumero)
    resultado = parImpar(numero)
    print(f"O numero {numero} é {resultado}")
    caracteres = contarCaracteres(entradatexto)
    print(f'O texto {entradatexto}, tem {caracteres} caracteres')
    
except:
    print("Erro: Digite um numero inteiro")
    print('Erro, digite uma palavra ou frase')