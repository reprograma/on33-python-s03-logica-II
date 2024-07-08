#Esta atividade consiste em criar um programa em Python que realiza duas tarefas principais:
#Verificar se um número fornecido pelo usuário é par ou ímpar.
#Contar os caracteres de um texto fornecido pelo usuário.
#Para isso, usaremos funções, condicionais (if e else), e tratamento de erros (try e except).

# Verificação se um número é par ou impar

def verificar_num_par_impar(numero): #criando estrutura lógica com condição para verificação de número para ou impar
    
  if numero % 10 == 0:
        return 'par'
  else:
        return 'impar'

entrada1 = input ('digite um número inteiro:') #criando a estrutura lógica de entrada para o usuário inserir a opção
entrada2 = input ('digite uma saudação:')

# Inserindo o try e o except para tentar converter a entrada em um numero e chamar a função verificar.num_par_impar.
try:
    numero = int(entrada1)
    resultado = verificar_num_par_impar(numero) # Chama a função e armazena o resultado
    print(f'O número {numero} é {resultado}.')
    
except ValueError:
    print('Erro: Por favor, insira um número inteiro válido.')
quantidade_caracter = len(entrada2) # Conta os caracteres 
print(f'A saudação "{entrada2}" possui {quantidade_caracter} caracteres.') # Imprime o resultado