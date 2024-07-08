print("Ola, Seja Bem-Vindo")

def verificar_parimpar(numero):
    if numero % 2 == 0:
        return "O número é par."
    else:
        return "O número é ímpar."

def contar_letra(texto):
    return len(texto)

def perguntas():
    try:
        numero_str = input("Digite um número inteiro para verificar se é par ou ímpar: ")
        numero = int(numero_str)
        
        texto = input("Agora digite um texto para contar os caracteres: ")
        
        resultado_par_impar = verificar_parimpar(numero)
        resultado_contagem = contar_letra(texto)
        
        print(resultado_par_impar)
        print("O texto possui {} caracteres.".format(resultado_contagem))
    
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

perguntas()