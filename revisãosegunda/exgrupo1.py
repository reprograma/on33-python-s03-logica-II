def idade_para_votar(idade_inteiro):
    if idade_inteiro >= 16:
        return 'pode votar.'
    else:
        return 'não pode votar.'
idade = input('Digite a sua idade: ')
try: 
    idade_inteiro = int(idade)
    resultado = idade_para_votar(idade_inteiro)
    print(f'Você {resultado} ')
except:
    print('Erro: Digite um número inteiro')