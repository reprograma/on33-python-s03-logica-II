try:
    # Tente executar este código
    numerador = 10
    denominador = 0
    resultado = numerador / denominador
    print(f"O resultado é {resultado}")
except ZeroDivisionError:
    # Se um erro de divisão por zero ocorrer, execute este código
    print("Erro: Não é possível dividir por zero.")
except TypeError:
    # Se um erro de tipo ocorrer, execute este código
    print("Erro: Tipo de dado inválido.")
