<h1 align="center">
  <img src="assets/reprograma-fundos-claros.png" alt="logo reprograma" width="500">
</h1>

# Tema da Aula

Turma Online On33 | Semana 03 | 2024 | [Professora Jenifer Plácido](https://www.linkedin.com/in/jenifer-pl%C3%A1cido-00b5611ab/)

# Aula: Condicionais, Operadores Lógicos e Depuração em Python 🐍

Bem-vindas On33! Nessa aula vamos explorar condicionais, operadores lógicos, tipos de erros, e técnicas de depuração, tudo isso de uma forma divertida e fácil de entender. Vamos lá! 🚀

## Objetivos 🎯

- Compreender e utilizar operadores de comparação.
- Implementar declarações condicionais simples e alternativas.
- Utilizar operadores lógicos em expressões condicionais.
- Identificar e entender diferentes tipos de erros em Python.
- Aprender a usar o debugger.
- Utilizar `try` e `except` para tratamento de erros.

---

## Condicionais 🔍

As condicionais permitem que seu programa tome decisões com base em condições. É como se o código perguntasse "E se isso acontecer?"

## `if`:

O `if` é usado para tomar decisões com base em uma condição. Se a condição for verdadeira, o código dentro do `if` será executado. Caso contrário, ele será ignorado.

### Estrutura Básica do `if`

```python
if condição:
    # código a ser executado se a condição for verdadeira
```

### Exemplo

Imagine que você quer saber se alguém é maior de idade. Você poderia escrever o seguinte código:

```python
idade = 20
if idade >= 18:
    print("Você é maior de idade!")
```

Neste exemplo, a condição `idade >= 18` é verdadeira porque `idade` é 20. Então, a mensagem "Você é maior de idade!" será exibida.

## `else`:

O `else` é usado junto com o `if` para fornecer uma alternativa. Se a condição do `if` for falsa, o código dentro do `else` será executado.

### Estrutura do `if` com `else`

```python
if condição:
    # código a ser executado se a condição for verdadeira
else:
    # código a ser executado se a condição for falsa
```

### Exemplo

Vamos expandir nosso exemplo anterior para incluir uma mensagem caso a pessoa não seja maior de idade:

```python
idade = 16
if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade.")
```

Neste exemplo, a condição `idade >= 18` é falsa porque `idade` é 16. Portanto, a mensagem "Você é menor de idade." será exibida.

O `if` e o `else` são usados para controlar o fluxo do seu programa. Eles permitem que seu código tome decisões e execute diferentes ações com base em condições específicas. Isso torna seu programa mais inteligente e flexível.

### Condicionais Encadeadas

Às vezes, temos mais de duas condições. Para isso, usamos `elif`.

```python
nota = 85
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
else:
    print("D")
```

---

## Operadores Lógicos 🤖

Os operadores lógicos nos ajudam a combinar várias condições. Vamos ver como usar `and`, `or` e `not`.

### Operador `and`

O `and` é verdadeiro se ambas as condições forem verdadeiras.

```python
nota = 85
presenca = 90
if nota >= 70 and presenca >= 75:
    print("Aprovado!")
else:
    print("Reprovado!")
```

### Operador `or`

O `or` é verdadeiro se pelo menos uma das condições for verdadeira.

```python
feriado = False
fim_de_semana = True
if feriado or fim_de_semana:
    print("Você pode descansar!")
else:
    print("Você tem que trabalhar!")
```

### Operador `not`

O `not` inverte o valor de uma condição.

```python
chovendo = False
if not chovendo:
    print("Você pode sair sem guarda-chuva!")
```

---

# Erros e Seus Tipos em Python ⚠️

Erros são uma parte natural da programação. Eles ocorrem quando o código não consegue executar a tarefa desejada por algum motivo. Compreender os tipos de erros pode ajudar a diagnosticar problemas no código e corrigi-los de forma mais eficaz. Vamos explorar os principais tipos de erros em Python e entender para que servem e como tratá-los.

## Erro de Sintaxe 🤔

### O que é?

Erros de sintaxe ocorrem quando o Python não consegue entender o código porque ele não segue as regras da linguagem. É como se você estivesse escrevendo uma frase em uma língua que o computador não entende.

Eles servem para nos alertar de que há algo errado na estrutura do nosso código, e precisamos corrigir isso antes que ele possa ser executado.

### Exemplo:

```python
if True
    print("Erro de sintaxe!")  # Faltou o ':' após 'True'
```

A mensagem de erro será algo como:

```
SyntaxError: invalid syntax
```

Para corrigir, adicione os dois pontos:

```python
if True:
    print("Erro de sintaxe corrigido!")
```

## Erro de Execução (Runtime Error) 🚨

### O que é?

Erros de execução ocorrem quando o código é sintaticamente correto, mas algo dá errado enquanto ele está rodando. Isso pode acontecer por diversas razões, como tentar dividir por zero ou acessar uma variável que não existe.

Eles servem para nos alertar de problemas que só aparecem durante a execução do programa, geralmente relacionados aos dados com os quais o programa está lidando.

### Exemplo:

```python
a = 1 / 0  # Erro de execução
```

A mensagem de erro será algo como:

```
ZeroDivisionError: division by zero
```

Para corrigir, evite dividir por zero:

```python
a = 1 / 1  # Código correto
```

## Erro Lógico 🤯

### O que é?

Erros lógicos ocorrem quando o código roda sem problemas, mas não faz o que deveria fazer. Esse tipo de erro é mais difícil de detectar porque não gera mensagens de erro.

Eles servem para nos alertar que, embora o código esteja livre de erros de sintaxe e de execução, ele não está funcionando conforme esperado, o que geralmente indica um problema na lógica do programa.

### Exemplo:

Vamos supor que você quer verificar se um número é par, mas comete um erro na condição:

```python
numero = 4
if numero % 2 != 0:
    print("O número é par.")  # Erro lógico
else:
    print("O número é ímpar.")
```

Embora o código rode sem erros, a lógica está incorreta.

Para corrigir, ajuste a condição:

```python
numero = 4
if numero % 2 == 0:
    print("O número é par.")  # Correto
else:
    print("O número é ímpar.")
```

## Erro de Importação 📦

### O que é?

Erros de importação ocorrem quando o Python não consegue encontrar o módulo que você está tentando importar.

Eles servem para nos alertar que estamos tentando usar um módulo ou biblioteca que não está disponível ou que foi digitado incorretamente.

### Exemplo:

```python
import non_existent_module  # Erro de importação
```

A mensagem de erro será algo como:

```
ModuleNotFoundError: No module named 'non_existent_module'
```

Para corrigir, verifique se o nome do módulo está correto ou se ele está instalado:

```python
import this  # Correto
```

## Erro de Tipo (TypeError) 🔤

### O que é?

Erros de tipo ocorrem quando você tenta realizar uma operação em um tipo de dado que não é compatível com essa operação.

Eles servem para nos alertar que estamos tentando realizar uma operação com tipos de dados que não são compatíveis entre si.

### Exemplo:

```python
a = "string" + 5  # Erro de tipo
```

A mensagem de erro será algo como:

```
TypeError: can only concatenate str (not "int") to str
```

Para corrigir, converta o número para string ou use apenas strings:

```python
a = "string" + str(5)  # Correto
```

---

Erros são uma parte inevitável da programação, mas compreender os diferentes tipos de erros pode tornar a depuração mais fácil e rápida. Saber o que cada erro significa e como corrigi-lo é uma habilidade fundamental para qualquer programador. Continue praticando e não se desespere com os erros – eles são oportunidades para aprender e melhorar seu código!

# Usando o Debugger no VS Code

## O que é um Bug? 🐞

Um **bug** é um erro ou falha no código que faz com que o programa funcione de maneira incorreta ou não funcione de todo. Bugs podem surgir de diversas formas, como erros de sintaxe, erros de execução, erros lógicos, entre outros. Encontrar e corrigir esses bugs é uma parte fundamental do trabalho de um programador.

## O que é um Debugger? 🛠️

Um **debugger** é uma ferramenta que ajuda os programadores a encontrar e corrigir bugs em seu código. Ele permite que você execute seu programa passo a passo, examine o fluxo de execução e inspecione as variáveis em tempo real.

O debugger serve para:

- **Identificar erros**: Encontrar onde e por que o código falha.
- **Entender o fluxo do programa**: Verificar a ordem de execução do código.
- **Inspecionar variáveis**: Verificar os valores das variáveis em diferentes pontos da execução.
- **Diagnosticar problemas**: Verificar a lógica do programa e garantir que ele esteja funcionando conforme o esperado.

## Como Utilizar o Debugger no VS Code? 🚀

Vamos aprender a usar o debugger no Visual Studio Code (VS Code) passo a passo.

### Passo 1: Instalar o VS Code

Se você ainda não tem o VS Code instalado, baixe e instale a partir do [site oficial](https://code.visualstudio.com/).

### Passo 2: Instalar a Extensão Python

Certifique-se de que a extensão Python do Microsoft está instalada no VS Code. Vá para a aba de Extensões (`Ctrl+Shift+X`) e procure por "Python". Instale a extensão da Microsoft.

### Passo 3: Configurar o Ambiente

1. **Abra o projeto ou arquivo Python** que você deseja depurar.
2. **Configure o Python Interpreter**: Selecione o interpretador Python certo para o seu projeto. Você pode fazer isso clicando no canto inferior esquerdo da janela do VS Code, onde está escrito a versão do Python, e selecionando o interpretador correto.

### Passo 4: Adicionar Pontos de Interrupção (Breakpoints)

Adicione pontos de interrupção clicando na margem esquerda ao lado do número da linha onde você deseja que a execução pause.

```python
def soma(a, b):
    resultado = a + b
    return resultado

x = 10
y = 5
z = soma(x, y)
print(f"O resultado é {z}")
```

Clique ao lado da linha `resultado = a + b` para adicionar um ponto de interrupção.

### Passo 5: Iniciar a Depuração

1. **Abrir a Paleta de Comandos**: Pressione `Ctrl+Shift+P` e digite "Debug: Start Debugging".
2. **Escolher a Configuração**: Selecione "Python File" para depurar o arquivo Python atual.

### Passo 6: Usar as Ferramentas do Debugger

Uma vez que a depuração iniciar, você verá a barra de ferramentas do debugger na parte superior do VS Code.

- **Continuar (`F5`)**: Continua a execução até o próximo ponto de interrupção.
- **Passar por cima (`F10`)**: Executa a próxima linha de código, mas não entra em funções.
- **Entrar (`F11`)**: Entra na próxima função chamada.
- **Sair (`Shift+F11`)**: Sai da função atual e retorna para a função chamadora.
- **Reiniciar (`Ctrl+Shift+F5`)**: Reinicia a sessão de depuração.
- **Parar (`Shift+F5`)**: Para a sessão de depuração.

### Passo 7: Inspecionar Variáveis e Pilha de Chamadas

- **Painel de Variáveis**: Veja os valores das variáveis na seção "Variables" na barra lateral esquerda.
- **Pilha de Chamadas**: Veja a pilha de chamadas na seção "Call Stack". Isso mostra a ordem das chamadas de funções.
- **Console de Depuração**: Execute comandos de Python diretamente no contexto atual do depurador.

### Passo 8: Utilizar Expressões de Observação (Watch)

Você pode adicionar variáveis ou expressões para monitorar no painel "Watch". Clique no `+` e digite o nome da variável ou expressão que deseja observar.

---

# Try e Except em Python

## O que é? 🧠

"Try" e "Except" são palavras-chave em Python usadas para tratar erros de forma elegante e controlada. Elas ajudam a garantir que seu programa não quebre quando encontra um erro e permite que você lide com o problema de maneira adequada.

Imagine que seu código é como dirigir um carro. Você pode encontrar obstáculos na estrada (erros). Usar "try" e "except" é como ter um plano de emergência para lidar com esses obstáculos sem parar completamente.

## Significado das Palavras

- **try**: Tentar. Você usa "try" para tentar executar um bloco de código que pode causar um erro.
- **except**: Exceto. Você usa "except" para especificar o que deve ser feito se um erro ocorrer no bloco "try".

## Como Funciona?

### Estrutura Básica

```python
try:
    # Tente executar este código
    ...
except:
    # Se um erro ocorrer, execute este código
    ...
```

#### Usando else e finally

- **else**: Um bloco opcional que é executado se não houver erros.
- **finally**: Um bloco opcional que é sempre executado, independentemente de erros.

```python
try:
    # Tente executar este código
    numerador = 10
    denominador = 2
    resultado = numerador / denominador
    print(f"O resultado é {resultado}")
except ZeroDivisionError:
    # Se um erro de divisão por zero ocorrer, execute este código
    print("Erro: Não é possível dividir por zero.")
else:
    # Se não houver erros, execute este código
    print("Divisão realizada com sucesso.")
finally:
    # Sempre execute este código, independentemente de erros
    print("Fim do bloco try-except.")
```

- **else**: Executado apenas se o bloco "try" não levantar nenhum erro. No nosso exemplo, "Divisão realizada com sucesso." será impresso porque `denominador` não é zero.
- **finally**: Sempre executado, independentemente de erros. No nosso exemplo, "Fim do bloco try-except." será sempre impresso.

Usar "try" e "except" em Python é como ter um plano de emergência. Eles ajudam a garantir que seu programa continue funcionando mesmo quando encontra problemas, permitindo que você lide com esses problemas de maneira controlada e elegante. Continuar praticando e usando essas ferramentas irá melhorar suas habilidades de programação e tornar seu código mais robusto e confiável.

# Sugestões de Atividades Simples Utilizando Try e Except

Aqui estão algumas atividades simples para praticar o uso de `try` e `except` junto com condicionais `if` e `else` em Python. Essas atividades são projetadas para ajudar iniciantes a entender como tratar erros e usar condicionais para controlar o fluxo do programa.

## Atividade 1: Divisão Segura

### Descrição

Crie um programa que pede ao usuário para inserir dois números e tenta dividir o primeiro pelo segundo. Use `try` e `except` para lidar com o erro de divisão por zero.

### Passos

1. Peça ao usuário para inserir dois números.
2. Tente dividir o primeiro número pelo segundo.
3. Use `try` e `except` para tratar a divisão por zero.
4. Exiba uma mensagem apropriada se o divisor for zero.

## Atividade 2: Entrada de Número Inteiro

### Descrição

Crie um programa que pede ao usuário para inserir um número inteiro e usa `try` e `except` para garantir que a entrada seja realmente um número inteiro.

### Passos

1. Peça ao usuário para inserir um número.
2. Use `try` e `except` para verificar se a entrada é um número inteiro.
3. Se a entrada não for um número inteiro, exiba uma mensagem de erro.

## Atividade 3: Verificação de Par ou Ímpar

### Descrição

Crie um programa que pede ao usuário para inserir um número inteiro e verifica se o número é par ou ímpar. Use `try` e `except` para garantir que a entrada seja um número inteiro.

### Passos

1. Peça ao usuário para inserir um número.
2. Use `try` e `except` para verificar se a entrada é um número inteiro.
3. Use `if` e `else` para verificar se o número é par ou ímpar.
4. Exiba uma mensagem apropriada.

## Atividade 4: Conversão de Temperatura

### Descrição

Crie um programa que pede ao usuário para inserir uma temperatura em graus Celsius e converte para Fahrenheit. Use `try` e `except` para garantir que a entrada seja um número.

### Passos

1. Peça ao usuário para inserir uma temperatura em graus Celsius.
2. Use `try` e `except` para verificar se a entrada é um número.
3. Converta a temperatura para Fahrenheit usando a fórmula: \( F = C \times \frac{9}{5} + 32 \).
4. Exiba a temperatura convertida.

# Atividades com Funções e Funções Internas de Python Utilizando Try, Except, If e Else

## Introdução

Vamos criar algumas atividades simples que envolvem funções em Python, uso de funções internas, e tratamento de erros com `try` e `except`. Estas atividades são projetadas para iniciantes e usam condicionais `if` e `else` para controlar o fluxo do programa.

## Atividade 1: Função de Soma

### Descrição

Crie uma função que soma dois números fornecidos pelo usuário. Use `try` e `except` para garantir que as entradas sejam números e exiba o resultado da soma.

### Passos

1. Crie uma função `soma` que recebe dois parâmetros.
2. Dentro da função, some os dois parâmetros e retorne o resultado.
3. Peça ao usuário para inserir dois números.
4. Use `try` e `except` para garantir que as entradas sejam números.
5. Chame a função `soma` e exiba o resultado.

## Atividade 2: Função de Verificação de Par ou Ímpar

### Descrição

Crie uma função que verifica se um número é par ou ímpar. Use `try` e `except` para garantir que a entrada seja um número.

### Passos

1. Crie uma função `verificar_par_impar` que recebe um parâmetro.
2. Use uma condicional `if` para verificar se o número é par ou ímpar e retorne a string apropriada.
3. Peça ao usuário para inserir um número.
4. Use `try` e `except` para garantir que a entrada seja um número.
5. Chame a função `verificar_par_impar` e exiba o resultado.

## Atividade 3: Função de Conversão de Temperatura

### Descrição

Crie uma função que converte uma temperatura de graus Celsius para Fahrenheit. Use `try` e `except` para garantir que a entrada seja um número.

### Passos

1. Crie uma função `celsius_para_fahrenheit` que recebe um parâmetro.
2. Converta a temperatura de Celsius para Fahrenheit usando a fórmula: \( F = C \times \frac{9}{5} + 32 \).
3. Retorne a temperatura convertida.
4. Peça ao usuário para inserir uma temperatura em graus Celsius.
5. Use `try` e `except` para garantir que a entrada seja um número.
6. Chame a função `celsius_para_fahrenheit` e exiba o resultado.



## Atividade 4: Função de Contagem de Caracteres

### Descrição

Crie uma função que conta o número de caracteres em uma string fornecida pelo usuário. Use `try` e `except` para garantir que a entrada seja uma string.

### Passos

1. Crie uma função `contar_caracteres` que recebe um parâmetro.
2. Use a função interna `len` para contar o número de caracteres na string e retorne o resultado.
3. Peça ao usuário para inserir uma string.
4. Use `try` e `except` para garantir que a entrada seja uma string.
5. Chame a função `contar_caracteres` e exiba o resultado.

---

### Recursos Adicionais

- [Documentação Oficial do Python](https://docs.python.org/3/)
- [Codecademy: Python](https://www.codecademy.com/learn/learn-python-3)
- [w3schools: Python](https://www.w3schools.com/python/)

Deixe o passado guardado, carregue apenas os aprendizados e se renove!
Bons estudos 🎉
