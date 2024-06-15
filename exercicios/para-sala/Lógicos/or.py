while True:
    nota = float(input("Insira uma nota de 1 a 10: "))
    if 1 <= nota <= 10:
        if nota >= 7:
            print("A aluna foi aprovada.")
        else:
            print("A aluna foi reprovada.")
        break
    else:
        print("Nota inválida. Por favor, insira uma nota entre 1 e 10.")