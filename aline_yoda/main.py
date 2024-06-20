def verificar_par_impar(numero):
    if numero % 2 == 0:
        return f"O número {numero} é par!"
    else:
        return f"O número {numero} é ímpar!"

def contar_caracteres(texto):
    return f'O texto "{texto}" possui {len(texto)} caracteres!'

while True:
    try:
        numero = int(input("Insira um número: "))
        texto = input("Insira um texto: ")

    except ValueError:
        print("Entrada inválida. Por favor, insira um número e um texto válidos.")

print(verificar_par_impar(numero))
print(contar_caracteres(texto))