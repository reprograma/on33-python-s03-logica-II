# Atividade 2: Cálculo de Média com Verificação de Aprovação
# Objetivo: Calcular a média de três notas e verificar se o aluno foi aprovado.

# Passos:

# Solicite ao usuário que insira três notas.
# Use uma função para calcular a média das notas.
# Use uma função para verificar se a média é suficiente para aprovação (média >= 7).
# Use try e except para tratar entradas inválidas.
# Exiba a média e se o aluno foi aprovado ou não.

# A função 'calcular_media' é definida. Ela recebe três argumentos: 'nota1', 'nota2' e 'nota3'.
# A função retorna a média dessas três notas.
def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

# A função 'verificar_aprovacao' é definida. Ela recebe um argumento chamado 'media'.
# A função verifica se a média é maior ou igual a 7. Se for, retorna "Aprovado". Caso contrário, retorna "Reprovado".
def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

# O bloco 'try' tenta executar algumas instruções.
try:
    # O programa pede ao usuário para digitar três notas. As notas são convertidas para números (floats) e armazenadas nas variáveis 'nota1', 'nota2' e 'nota3'.
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
    # A função 'calcular_media' é chamada com 'nota1', 'nota2' e 'nota3' como argumentos. O resultado é armazenado na variável 'media'.
    media = calcular_media(nota1, nota2, nota3)
    # A função 'verificar_aprovacao' é chamada com 'media' como argumento. O resultado é armazenado na variável 'status'.
    status = verificar_aprovacao(media)
    
    # O programa imprime a média e o status do aluno.
    print(f"Sua média é {media:.2f}. Você está {status}.")
# Se ocorrer um erro (por exemplo, se o usuário digitar algo que não seja um número para as notas),
# o bloco 'except' será executado.
except:
    # Neste caso, uma mensagem de erro é impressa.
    print("Por favor, insira notas válidas.")
