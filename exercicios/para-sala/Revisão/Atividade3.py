# Atividade 2: Conversor de Medidas
# Objetivo: Criar um programa que converte diferentes 
# unidades de medida (metros para quilômetros, gramas para quilogramas, etc.).

# Passos:

# Solicite ao usuário que insira um valor e escolha uma unidade de medida.
# Verifique se a unidade de medida é válida.
# Use funções para realizar a conversão.
# Exiba o resultado da conversão.
# A função 'metros_para_kilometros' é definida. Ela recebe um argumento chamado 'metros'.
# A função retorna a conversão de metros para quilômetros.
def metros_para_kilometros(metros):
    return metros / 1000

# A função 'gramas_para_kilogramas' é definida. Ela recebe um argumento chamado 'gramas'.
# A função retorna a conversão de gramas para quilogramas.
def gramas_para_kilogramas(gramas):
    return gramas / 1000

# A função 'converter' é definida. Ela recebe dois argumentos: 'valor' e 'unidade'.
# A função verifica a unidade e chama a função de conversão correspondente.
def converter(valor, unidade):
    if unidade == 'metros':
        return metros_para_kilometros(valor)
    elif unidade == 'gramas':
        return gramas_para_kilogramas(valor)
    else:
        return "Unidade de medida inválida."

# O bloco 'try' tenta executar algumas instruções.
try:
    # O programa pede ao usuário para digitar um valor e uma unidade.
    valor = float(input("Digite o valor a ser convertido: "))
    unidade = input("Escolha a unidade de medida (metros/gramas): ")
    # A função 'converter' é chamada com 'valor' e 'unidade' como argumentos. O resultado é armazenado na variável 'resultado'.
    resultado = converter(valor, unidade)
    # O programa imprime o resultado da conversão.
    print(f"O resultado da conversão é: {resultado}")
# Se ocorrer um erro (por exemplo, se o usuário digitar algo que não seja um número para o valor),
# o bloco 'except' será executado.
except:
    # Neste caso, uma mensagem de erro é impressa.
    print("Por favor, insira um valor válido.")


