# Esta é uma função chamada 'soma' que recebe dois argumentos: 'a' e 'b'.
# A função retorna a soma desses dois números.
def soma(a, b):
    return a + b

# Aqui, o programa pede ao usuário para digitar o primeiro número.
# O valor digitado é armazenado na variável 'entrada1'.
entrada1 = input("Digite o primeiro número: ")

# O programa faz o mesmo para o segundo número, armazenando o valor em 'entrada2'.
entrada2 = input("Digite o segundo número: ")

# O bloco 'try' tenta executar algumas instruções.
try:
    # Aqui, o programa tenta converter as entradas do usuário para números (floats).
    # Se as entradas puderem ser convertidas para números, elas são armazenadas nas variáveis 'numero1' e 'numero2'.
    numero1 = float(entrada1)
    numero2 = float(entrada2)

    # A função 'soma' é chamada com 'numero1' e 'numero2' como argumentos, e o resultado é armazenado na variável 'resultado'.
    resultado = soma(numero1, numero2)

    # O resultado da soma é então impresso na tela.
    print(f"A soma de {numero1} e {numero2} é: {resultado}")

# Se ocorrer um erro ao tentar converter as entradas para números (ou seja, se o usuário digitou algo que não é um número),
# o bloco 'except' será executado.
except ValueError:
    # Neste caso, uma mensagem de erro é impressa na tela.
    print("Erro: Por favor, insira números válidos.")
 