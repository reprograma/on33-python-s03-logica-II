# Crie um programa que pede ao usuário para inserir dois números 
# e tenta dividir o primeiro pelo segundo. Use try e except 
# para lidar com o erro de divisão por zero.

# Solicitar dois números ao usuário
numerador = float(input("Digite o numerador: "))
denominador = float(input("Digite o denominador: "))

# Tentar realizar a divisão
try:
    resultado = numerador / denominador
    print(f"O resultado da divisão é: {resultado}")
except:
    print("Erro: Não é possível dividir por zero.")
