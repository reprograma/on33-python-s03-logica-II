def par_impar (numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'ímpar'
def contar_caracteres (texto):
    return len(texto)

entrada1 = input('Digite um número inteiro: ')
entrada2 = input('Digite um texto: ')

try:
    numero = int(entrada1)
    resultado = par_impar(numero)
    
    caracteres = contar_caracteres(entrada2)
        
    print(f'O número {numero} é {resultado}, e a string {entrada2} tem {caracteres} caracteres.')
       
except:
    print('Erro: Digite um número inteiro.')































