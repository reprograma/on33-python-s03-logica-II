print ("Olá, seja bem-vinda ao Programa Número e Letra!")
print ("Aqui você descobre se um número é Par ou Ímpar e quantos números tem a sua frase favorita! Vamos começar?")

def identificação (numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

entrada1 = input ("Digite um número: ")    
try: 
    numero = int(entrada1)
    resultado1 = identificação(numero)
    print(f"O número escolhido é {resultado1}")
except: 
    print("Número incorreto, verifique novamente!")

def contarletras(texto):
    return len(texto)
entrada2 = input ("Digite sua frase favorita: ")
try:
    resultado2 = contarletras(entrada2)
    print(f"Sua frase favorita {entrada2}, têm {resultado2} letras.")
except: 
    print("Termo incorreto, verifique novamente!")
