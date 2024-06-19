def verificar_par_impar(numero):
    if numero % 2 == 0:
        return f"O número {numero} é par. "
    else:
        return f"O número {numero} é ímpar. "

def contar_caracteres(texto):
    return len(texto)

try:
    numero = int(input("Insira um número: "))
    texto = input("Insira um texto: ")

    resultado_par_impar = verificar_par_impar(numero)
    resultado_contagem = contar_caracteres(texto)

    print(resultado_par_impar)
    print(f'O texto "{texto}" possui {resultado_contagem} caracteres. ')

except ValueError:
    print("Erro: Insira um número válido.")
except Exception as e:
    print(f"Erro inesperado: {e}")
