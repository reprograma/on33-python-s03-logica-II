print('Olá e seja bem-vindo!')

numero = input('Digite um número: ')
texto = input('Digite uma palavra ou frase: ')

def parImpar (numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'ímpar'

def contarCaracteres(texto):
        return len(texto)

try:
    if numero == '' or texto == '':
        print('Nenhum número ou letra fornecidos.')
    if numero.isdigit() == False:
        print('Digite apenas númeos.') 
    if texto.isalpha() == False:
        print('Digite apenas letras.')
    else: 
        num = int(numero)
        resultado = parImpar(num)
        caratcteres = contarCaracteres(texto)
        print(f'O número {num} é {resultado} e a palavra ou frase "{texto}" tem {caratcteres} caracteres.')
except:
    print('Erro na digitação!')