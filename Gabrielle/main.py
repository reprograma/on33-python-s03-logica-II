# Esta atividade consiste em criar um programa em Python que realiza duas tarefas principais: 
# 1)Verificar se um número fornecido pelo usuário é par ou ímpar.
# 2) Contar os caracteres de um texto fornecido pelo usuário.
# `verificar_par_impar(numero)`: Função que verifica se um número é par ou ímpar.
# `contar_caracteres(texto)`: Função que conta os caracteres de um texto.

def verificar_par_impar(numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'impar'
    
def contar_caracteres(texto):
    return len(texto)

entrada_numero = input('Digite um número inteiro: ')
texto = input('Digite um texto: ')

try:
    numero = int(entrada_numero)
    resultado_numero = verificar_par_impar(numero)
    print(f'O número {numero} é {resultado_numero}.🎉')

except ValueError:
    print('Digite um número inteiro válido.')


try:
    caracteres = contar_caracteres(texto)
    print(f'A string "{texto}" possui {caracteres} caracteres.📝')

# Como a função input só retorna strings, independentemente do tipo de entrada do usuário, a função nunca cairá no except.
except :
    print(f'Erro: digite uma palavra ou frase válida.')


