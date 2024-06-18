#ATIVIDADE PARA CASA

# Verificação de Número e Texto
# Esta atividade envolve duas partes:
# 1. Verificar se um número fornecido pelo usuário é par ou ímpar.
# 2. Contar os caracteres de um texto fornecido pelo usuário.
# Você usará funções, condicionais (if e else), e tratamento de erros (try e except) para garantir que as entradas sejam válidas.Passos
# 1. Crie uma função para verificar se um número é par ou ímpar.
# 2. Crie uma função para contar os caracteres de um texto.
# 3. Solicite ao usuário para inserir um número e um texto.
# 4. Use try e except para tratar entradas inválidas.
# 5. Chame as funções e exiba os resultados.
def verificar_par_impar(numero):   # função verifica se e par ou impar
    if numero % 2 == 0:
        return "par"   # retorna par se o número for dividido por 2
    else:
        return "ímpar"  # retorna impar se o número não for dividio por 2

def contar_caracteres(texto): # função conta o número de caracteres 
    return len(texto)              # retorna o comprimento
  
try:
    numero = int(input("Digite um número inteiro: "))
    texto = input("Digite um texto: ")

    if texto.isdigit():    #isdigit() é um método em strings no Python que verifica se todos os caracteres na string são dígitos (0-9).
        print("Insira uma frase, não apenas números.")
    else:
         
         resultado_par_impar = verificar_par_impar(numero)   # chama a função
         resultado_contagem = len(texto) - texto.count(" ")  #  Calcula o número de caracteres no texto, excluindo espaços, e armazena o resultado na variável resultado_contagem


         print(f"O número {numero} é {resultado_par_impar}. \U0001F609")
         print(f'O texto "{texto}" possui {resultado_contagem} caracteres. \U0001F4DD')

except ValueError:
    print("Erro: Digite um número inteiro válido.")
except:
    print("Erro: Digite uma palavra ou frase válida.")



# # obtem tamanho do texto e subtri a contagem de espaços
#  ex textoTam = len (texto) - texto.count(" ")
#  print(textoTam)
#   o método strip apenas remove os espaços no começo e fim da string
#   ex texto= '123 456 78'
#   qtdletras = len(texto.strip())

# Neste caso, o ideal é usar o método replace, que irá substituir todos os espaços por um caractere escolhido 
# (ou nenhum caractere neste caso), da seguinte forma.
#   numero_caractere = len(texto.replace(" ", " ")) # troca espaço por nada 
#   print(numero_caractere)
