# Criar função para verificar se é par ou ímpar
def par_ou_impar(numero):
    if numero % 2 == 0:  # % é utilizado p/ obter o resto de uma divisão entre dois números
        return 'par' #resposta sobre o numero inserido
    else:
        return 'ímpar' #resposta sobre o numero inserido

# Criar função para contar caracteres
def contar_caracteres(texto):
    return len(texto)  # len é utilizado p/ contar o número de caracteres

while True:  # Cria loop infinito
    try:
        numero = int(input('Insira um número: '))
        break  # Permite sair do loop while/enquanto quando a entrada for válida
    except ValueError:
        print('Entrada inválida. Por favor, insira um número inteiro.')

texto = input('Insira um texto: ')

resultado_par_ou_impar = par_ou_impar(numero)
contagem_caracteres = contar_caracteres(texto)

print(f'O número {numero} é {resultado_par_ou_impar}.')#O f antes da string realiza uma formataçao, permitindo inserir variáveis dentro da string
print(f'O texto inserido tem {contagem_caracteres} caracteres.')
