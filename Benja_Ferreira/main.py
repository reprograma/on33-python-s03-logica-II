def verificar_par_impar(numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'impar'
    
def contar_caracteres(texto):
    return len(texto)

entrada1 = input('Digite um número: ')
entrada2 = input('Digite uma palavra ou frase: ')

try:
    numero = int(entrada1)
    resultado = verificar_par_impar(numero)
    print(f'O número {numero} é {resultado}')
except:
    print('Erro, digite um número inteiro')


try:
     caracteres = contar_caracteres(entrada2)
     print(f'O texto {entrada2}, tem {caracteres} caracteres')
except:
     print('Erro, digite uma plavra ou frase')