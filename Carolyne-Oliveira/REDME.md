# 📝 Verificação de Números e Texto

## 📚 Descrição da Atividade

Verificar se um número fornecido pelo usuário é par ou ímpar. Contar os caracteres de um texto fornecido pelo usuário.
Você usará funções, condicionais (if e else), e tratamento de erros (try e except) para garantir que as entradas sejam válidas.

## 📋 Passo a Passo

 1 Crie uma função para verificar se um número é par ou ímpar.

    # def verificar_par_impar(numero):
        # if numero % 2 == 0:
            # return f"O número {numero} é par."
        # else:
            # return f"O número {numero} é ímpar."

 2 Crie uma função para contar os caracteres de um texto.

    # def contar_caracteres(texto):
        # return f"O texto fornecido tem {len(texto)} caracteres."

 3 Solicite ao usuário para inserir um número e um texto.

    # numero_usuario = input("Insira um número: ")
    # texto_usuario = input("Insira um texto: ")

 4 Use try e except para tratar entradas inválidas.

    # try:
        # numero_validado = int(numero_usuario)
        # resultado_par_impar = verificar_par_impar(numero_validado)
        # resultado_contagem = contar_caracteres(texto_usuario)
    # except ValueError:
        # print("Erro: A entrada não é um número inteiro válido.")

 5 Chame as funções e exiba os resultados.
  
    # print(resultado_par_impar)
    # print(resultado_contagem)

# 📜 POEMA:
“O Zen do Python” de Tim Peters:

O belo é melhor que o feio. 
Explícito é melhor que implícito. 
Simples é melhor que complexo. 
Complexo é melhor que complicado. 
Plano é melhor que aninhado. 
Esparso é melhor que denso. 
Legibilidade conta. 
Casos especiais não são especiais o suficiente para quebrar as regras. 
Embora a praticidade vença a pureza. 
Erros nunca devem passar silenciosamente. 
A menos que sejam explicitamente silenciados. 
Diante da ambiguidade, recuse a tentação de adivinhar. 
Deve haver um – e preferencialmente apenas um – modo óbvio de fazer isso. 
Embora esse modo possa não ser óbvio no início, a menos que você seja holandês. 
Agora é melhor que nunca. Embora nunca seja frequentemente melhor que agora mesmo. 
Se a implementação é difícil de explicar, é uma má ideia. 
Se a implementação é fácil de explicar, pode ser uma boa ideia. 
Namespaces são uma ideia muito boa – vamos fazer mais desses!  


📜 The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.  
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
