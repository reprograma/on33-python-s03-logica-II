# mensagem inicial
print("Vamos brincar de Par ou ímpar?\n")

# função 1
def soma (a, b):
    return a + b

# função 2
def parOuImpar (soma):
    if resultadoSoma % 2 == 0:
        return "par"
    else:
        return "ímpar"
    
#função 3
def contCaractere(texto):
    return len(texto)

# PARTE 1 - Jogo
while True:
    num = input("Eu escolho par e joguei 5. É sua vez, jogue um número qualquer: ")
    try:
        resultadoSoma = soma (float(num), 5)
        resultadoImparPar = parOuImpar (resultadoSoma)
        if resultadoImparPar == 'par':
            print(f'\nDeu {resultadoSoma} e é Par, ganhei! \nAgora vou te desafiar:')
            break
        else:
            print(f'\nDeu {resultadoSoma} e é Ímpar, perdi! \nMe desafia:')
            break
    except (ValueError, TypeError):
        print('Opa, acho que você inseriu um valor errado.')
        continue

# PARTE 2 - Desafio

#entrada usuário 2 - desafio
entrada = input('Digita qualquer frase e eu adivinho o número de caracteres: ')

# erro e exceção 2
try:
    resultadoNumCaract = contCaractere (entrada)
    
    if resultadoNumCaract == 1:
        print(f'Seu texto "{entrada}" contém {resultadoNumCaract} caractere.\n')
    else:
        print(f'Seu texto "{entrada}" contêm {resultadoNumCaract} caracteres.\n')
except ValueError:
    print('Opa, acho que você inseriu o texto errado. Tenta de novo')
else:
    print('Viu só, arrasei nesse jogo!')
finally:
    print('Obrigada por jogar comigo. Até logo!')