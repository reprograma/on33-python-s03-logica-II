# Atividade 1: Verificação de Idade para Votação
# Objetivo: Verificar se a idade do usuário permite que ele vote.

# Passos:

# Solicite ao usuário que insira sua idade.
# Use uma função para verificar se a idade do usuário é 16 ou mais.
# Use try e except para tratar entradas inválidas.
# Exiba uma mensagem indicando se o usuário pode votar ou não.

# A função 'pode_votar' é definida. Ela recebe um argumento chamado 'idade'.
# A função verifica se a idade é maior ou igual a 16. Se for, retorna "Você pode votar." Caso contrário, retorna "Você ainda não pode votar."
def pode_votar(idade):
    if idade >= 16:
        return "Você pode votar."
    else:
        return "Você ainda não pode votar."

# O bloco 'try' tenta executar algumas instruções.
try:
    # O programa pede ao usuário para digitar sua idade. A idade é convertida para um número inteiro e armazenada na variável 'idade'.
    idade = int(input("Digite sua idade: "))
    # A função 'pode_votar' é chamada com 'idade' como argumento. O resultado é armazenado na variável 'mensagem'.
    mensagem = pode_votar(idade)
    # O programa imprime a mensagem.
    print(mensagem)
# Se ocorrer um erro (por exemplo, se o usuário digitar algo que não seja um número para a idade),
# o bloco 'except' será executado.
except:
    # Neste caso, uma mensagem de erro é impressa.
    print("Por favor, insira um número válido para a idade.")