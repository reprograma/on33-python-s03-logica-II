A atividade consiste em criar um programa em Python que realiza duas tarefas principais:

Verificar se um número fornecido pelo usuário é par ou ímpar.
Contar os caracteres de um texto fornecido pelo usuário. Para estruturar o programa foi utilizado as funções condicionais (if e else), a len (para contar os caracteres do texto de entrada-saudação) e a função de tratamento de erros (try e except).
Entrada: Verificação se um número é par ou impar: Cria uma função utilizando o def em seguida estrutura as condições utilizando o if e o else. Lembrar de utilizar a instrução 'return' dentro da função. Assim é possível retornar um valor específico correspondente aos argumentos destacados nas condições.

Exemplo: def verificar_impar-par(numero)

if numero % 4 == 0: return 'par' else: return 'impar'

Criar os input com as entradas requeridas Exemplo:

Entrada1 = input () entrada2 = input ()

Inserir as funções try e o except para tentar converter a entrada em um numero e chamar a função verificar.

No bloco que contém o try - contém o código que pode gerar uma exceção ou um erro. Dessa forma, o Python tentará executar esse código, e se um erro ocorrer, interromperá a execução deste bloco e moverá para o bloco except. O bloco que contém o código except será executado se um erro ocorrer no bloco try. Dessa forma, o código não será quebrado.

Exemplo: try:

código que pode gerar um erro
resultado = 4 / 0
except ZeroDivisionError: # código que é executado se houver ZeroDivisionError print("Não é possível dividir por zero.")

Inserindo a função len

Para quantificar os caracteres da entrada2-saudação utilizaremos a função len(), pois ela retorna o tamanho do objeto, ou seja, a quantidade dos caracteres. Ao final, lembrar de solicitar a impressão da frase desejada. Exemplo: print (A saudação tal {entrada2} possui {} tantos carcteres).