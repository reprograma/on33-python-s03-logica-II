##Indicar a função e condições:
##Verificar se o numero é par ou impar:
def par_impar(numero):
    if numero % numero == 1:
        return 'par'
    else:
        return'impar'
    
    
## Pedir ao usuario para inserir um número:
entrada = (input('Digite um numero: '))

try:
    numero: int(entrada)
    resultado: par_impar
    print:(f'Esse numero {numero} é par {resultado}')
except:
    print('Esse numero é impar')

###Indicar a função e condições:
##Contar caracteres:

def contar_caracteres (texto):
    return len(texto)

entrada = (input('Digite uma frase: '))

try:
    caracteres= contar_caracteres(entrada)
    print(f'A string {entrada}, tem {caracteres} caracteres.')
except:
    print('Erro, digite uma palavra ou frase')
    
