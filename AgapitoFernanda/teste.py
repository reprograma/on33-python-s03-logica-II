while True:
    # Loop principal do programa
    try:
        # Solicita e valida a entrada do número
        entradaNum = input("Digite um número: ")
        numero = int(entradaNum)
    except ValueError:
        print("Erro: Por favor, insira um número inteiro válido.")
        continue  # Volta para o início do loop se a entrada for inválida

    # Solicita e valida a entrada da palavra ou frase
    entrada = input("Digite uma palavra ou frase: ")

    # Função para verificar se o número é par ou ímpar
    def verificar_par_impar(numero):
        if numero % 2 == 0:
            return "par"
        else:
            return "ímpar"

    # Verifica e exibe o resultado do número
    resultado = verificar_par_impar(numero)
    print(f"O número {numero} é {resultado}.")

    # Função para contar o número de caracteres na palavra ou frase
    def contar_caracteres(texto):
        return len(texto)

    # Conta e exibe o número de caracteres na palavra ou frase
    try:
        caracteres = contar_caracteres(entrada)
        if not entrada.isalpha():
            print("Digite apenas letras.")
        else:
            print(f"A palavra '{entrada}' tem {caracteres} caracteres.")
    except TypeError:
        print("Erro: Por favor, insira uma string válida.")

    # Pergunta se o usuário deseja continuar o loop
    continuar = input("Deseja continuar? (sim/não): ").lower()
    if continuar != "sim":
        break  # Sai do loop se o usuário digitar "não"

print("Obrigado por usar o programa!")
