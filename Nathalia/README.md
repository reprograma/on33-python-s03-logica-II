# Introdução

Programa gerado para a ***Atividade 03 da Semana 03*** - Turma 033 - Reprograma - Análise de dados em Python

*Tema de Estudo:* Tratamento de erros e exceções, funções e operadores.

# Programa

***Jogando par ou ímpar (main.py)***

Objetivo: Interagir com o usuário para um jogo popular de par ou ímpar.

Para efeitos de simplificação o código já apresenta a jogada do programa, não necessitando assim de um segundo usuário.

O programa deve calcular as entradas (programa e usuário) e apresentar se o resultado é impar ou par, respondendo com um desafio: Que o programa 'adivinhe' a quantidade de caracteres de um texto inserido.

A primeira resposta é condição obrigatória, por isso ele deve solicitar uma inserção válida para rodar.

# Estrutura do programa

* Mensagem inicial convidando ao jogo;
* Informa a escolha do programa e solicita a entrada de um ***número***;
* Apresenta o resultado e quem ganhou o jogo;
* Convida para um desafio;
* Usuário informa uma entrada em texto;
* Programa contabiliza o número de caracteres e apresenta resultado;
* Mensagem caso não apresente erro;
* Mensagem de finalização em todos os casos.

# Informações do Código

Linguagem: *Python 3.12.4*

Funções utilizadas: 

- *input()* para entrada de dados pelo usuário 

- *print()* para apresentar os resultados das entradas

- *soma()* para calcular a entrada de dados do usuário e interagir

- *parOuImpar*() para verificar se o resultado da *soma()* é par ou ímpar
- *contCaractere()* para contabilizar a quantidade de caracteres digitados pelo usuário
- *while* para não executar o código com erro na primeira resposta *condição obrigatória
- *try, exception, else e finally* para tratamento de erros e exceções

Formatos: *String* e *Float*

Quebras de linha *\n* nas saídas de dados para melhor visualização final ao usuário.