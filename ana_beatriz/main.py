
def par_ou_impar(numero):
    try:
        numero = int(numero) 
        if numero % 2 == 0:
            print('Esse número é par')

        else: 
            print('Este número é impar')

    except:
        print("Erro: O número fornecido não é inteiro.")

numero = input('Insira um número: ')
par_ou_impar(numero)      

#descobrir o número de letras de um texto

def contar_letras(texto):
            return len(texto)
try:
     texto = str(input('Insira um texto: '))
     quantidade_letras = contar_letras(texto)
     print(f'O seu texto contêm {quantidade_letras} letras')

except: 
    print("Erro: Insira apenas um texto que contenha letras")

contar_letras(texto)
