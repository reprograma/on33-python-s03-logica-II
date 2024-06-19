def par_impar (numero):
    if numero % 2 == 0:
        return "par"
    else: 
        return "impar"

entradaNumero = input("Digite um número: ")

try:
    numero = int(entradaNumero)
    resultado = par_impar(numero)
    print(f" Voçe escolheu {numero} esse número é  {resultado}. ")

except:
     print("Digite número inteiro para validar a regra")


#entradaTexto = input("Digite seu texto: ")

#qtd_caracteres = len(entradaTexto)

texto1 = input("digite mensagem: ")
mensagem = input("complemento: ")

soma = texto1 + mensagem

print(f"A mensagem: {texto1} {mensagem} possue {len(soma)} caracteres. ")





