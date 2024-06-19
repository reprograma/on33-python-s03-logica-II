def par_impar(numero):
   if numero % 2 == 0:
     return 'Par'
   else:
      return 'Ímpar'
 

entrada = input('Digite um número inteiro: ')

try: 
    numero = int(entrada)
    resultado = par_impar(numero)
    print(f'O número {numero} é {resultado}')

except:
    print('Favor digitar um número inteiro!')


def contarCaracteres(texto):
    return len(texto)

entrada = len(input('Digite uma palavra ou uma frase: '))

try:
    caracteres = contarCaracteres(entrada)
    print(f'A frase {entrada}, tem {caracteres} caracteres')
except:
    print('Erro, digite uma palavra ou frase!')
   


