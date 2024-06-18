# Verificar se um número fornecido pelo usuário é par ou ímpar.
# Contar os caracteres de um texto fornecido pelo usuário.
# Você usará funções, condicionais (if e else), e tratamento de erros (try e except) para garantir que as entradas sejam válidas.

# 1 Crie uma função para verificar se um número é par ou ímpar.
def verificar_par_impar(numero):
    if numero % 2 == 0:
        return f"O número {numero} é par."
    else:
        return f"O número {numero} é ímpar."

# 2 Crie uma função para contar os caracteres de um texto.
def contar_caracteres(texto):
    return f"O texto fornecido tem {len(texto)} caracteres."

# 3 Solicite ao usuário para inserir um número e um texto.
numero_usuario = input("Insira um número: ")
texto_usuario = input("Insira um texto: ")

# 4 Use try e except para tratar entradas inválidas.
try:
    numero_validado = int(numero_usuario)
    resultado_par_impar = verificar_par_impar(numero_validado)
    resultado_contagem = contar_caracteres(texto_usuario)
except ValueError:
    print("Erro: A entrada não é um número inteiro válido.")

# 5 Chame as funções e exiba os resultados.
print(resultado_par_impar)
print(resultado_contagem)
