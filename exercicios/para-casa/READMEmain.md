# Verificador de Par/Ímpar e Contador de Caracteres

Este script em Python realiza duas funções principais:

1. Verifica se um número inteiro é par ou ímpar.
2. Conta o número de caracteres em uma palavra ou frase.

## Funcionalidades

### Função `verificar_par_impar`

Esta função verifica se um número inteiro é par ou ímpar.

- Parâmetros

  :

  - `numero` (int): O número a ser verificado.

- Retorno

  :

  - (str): Retorna `"par"` se o número for par, ou `"ímpar"` se o número for ímpar.

### Função `contar_caracteres`

Esta função conta o número de caracteres em uma string.

- Parâmetros

  :

  - `texto` (str): A palavra ou frase cuja quantidade de caracteres será contada.

- Retorno

  :

  - (int): O número de caracteres na string fornecida.

## Uso

1. O script solicita ao usuário que insira um número inteiro e uma palavra ou frase.
2. Verifica se o número é par ou ímpar usando a função `verificar_par_impar`.
3. Conta o número de caracteres na palavra ou frase usando a função `contar_caracteres`.
4. Exibe os resultados.



### Explicação do Código

1. **Definição das Funções**:
   - `verificar_par_impar`: Esta função utiliza o operador módulo `%` para determinar se o número é par (`numero % 2 == 0`) ou ímpar.
   - `contar_caracteres`: Esta função utiliza a função `len()` para contar o número de caracteres na string fornecida.
2. **Entrada do Usuário**:
   - `entrada_n` e `entrada_txt` são usadas para capturar as entradas do usuário (um número inteiro e uma palavra/frase, respectivamente).
3. **Bloco `try`**:
   - Tenta converter `entrada_n` para um inteiro.
   - Chama `verificar_par_impar` e `contar_caracteres` com as entradas apropriadas.
   - Exibe os resultados.
4. **Bloco `except`**:
   - Captura qualquer exceção (por exemplo, se o usuário inserir uma entrada inválida).
   - Exibe uma mensagem de erro informando ao usuário que deve fornecer entradas válidas.

## Requisitos

- Python 3.x

## Execução

Para executar o script, salve-o em um arquivo `.py` e execute-o usando um interpretador Python:

`python nome_do_arquivo.py`