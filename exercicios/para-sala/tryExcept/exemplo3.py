try:
    # Tente executar este código
    numerador = 10
    denominador = 2
    resultado = numerador / denominador
    print(f"O resultado é {resultado}")
except:
    # Se um erro de divisão por zero ocorrer, execute este código
    print("Erro: Não é possível dividir por zero.")
else:
    # Se não houver erros, execute este código
    print("Divisão realizada com sucesso.")
finally:
    # Sempre execute este código, independentemente de erros
    print("Fim do bloco try-except.")
