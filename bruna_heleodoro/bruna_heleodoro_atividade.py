def verificar_numero(numero):
    try:
        numero = int(numero)
    except ValueError:
        return 'Valor inválido. Insira um número inteiro válido.'
    
    if numero % 2 == 0:
        return f'{numero} é um número par.'
    else:
        return f'{numero} é um número impar.'

def contar_caracter(texto):
    return len(texto)

def menu():
    print('===============================================================================================')   
    print('                BEM VINDO AO SISTEMA ON33 - LÓGICA SEMANA II                                   ')
    print('===============================================================================================')   
    print('                                    MENU                                                       ')
    print('                          1. VERIFICAR PARIDADE                                      ')
    print('                          2. CONTAR CARACTERES                                       ')
    print('                          3. SAIR DO SISTEMA                                         ')
    print('===============================================================================================')   
    try:
        opcao = int(input('Escolha uma opção acima: '))
        return opcao
    except ValueError:
        print('\nErro: Valor inválido. Insira um número inteiro válido.\n')
        return menu()


def executar_opcao(opcao):
    if opcao == 1:
        num_usuario = input('Digite um número: ')
        resultado = verificar_numero(num_usuario)
        print(resultado)
    elif opcao == 2:
        texto = input('Digite um texto: ')
        numero_caracteres = contar_caracter(texto)
        print(f'O texto possui {numero_caracteres} caracteres.')
    elif opcao == 3:
        print('Saindo do sistema...')

opcao = menu()
executar_opcao(opcao)