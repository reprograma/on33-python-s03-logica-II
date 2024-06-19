def verificar_par_impar(numero):
    if numero % 2 == 0:
        return f"O número {numero} é par. 🎉"
    else:
        return f"O número {numero} é ímpar. 🎉"

def contar_caracteres(texto):
    quantidade = len(texto)
    return f'O texto "{texto}" possui {quantidade} caracteres. 📝'

def main():
    try:
        numero = int(input("Insira um número: "))
        
        texto = input("Insira um texto: ")
        
        resultado_numero = verificar_par_impar(numero)
        
        resultado_texto = contar_caracteres(texto)
        
        print(resultado_numero)
        print(resultado_texto)
        
    except ValueError:
        print("Erro: Entrada inválida. Certifique-se de inserir um número válido.")

main()