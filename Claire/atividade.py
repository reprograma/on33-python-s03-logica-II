def verificar_par_ou_impar():
    try:
        numero = int(input("Digite um número: "))
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
        else:
            print(f"O número {numero} é ímpar.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

def contar_caracteres():
    texto = input("Digite um texto: ")
    if texto:
        numero_de_caracteres = len(texto)
        print(f"O texto fornecido contém {numero_de_caracteres} caracteres.")
    else:
        print("Entrada vazia. Por favor, insira um texto.")

def main():
    verificar_par_ou_impar()
    contar_caracteres()

if __name__ == "__main__":
    main()
