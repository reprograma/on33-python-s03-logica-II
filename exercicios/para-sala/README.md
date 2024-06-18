### Funções em Python

#### O que são Funções?

Funções são blocos de código que realizam uma tarefa específica. Elas ajudam a organizar e reutilizar o código, tornando-o mais limpo e fácil de manter. Pense nas funções como "receitas" que você pode usar várias vezes para obter o mesmo resultado.

#### Para que servem as Funções?

- **Organização**: Dividem o código em partes menores e mais gerenciáveis.
- **Reutilização**: Permitem usar o mesmo código em diferentes partes do programa sem ter que reescrever.
- **Clareza**: Tornam o código mais fácil de ler e entender.

### Funções Internas

Funções internas (ou embutidas) são aquelas que já vêm prontas no Python. Você não precisa defini-las, apenas usá-las. Elas são como ferramentas básicas que você sempre tem à mão.

#### Exemplos de Funções Internas

1. **`print()`**: Exibe mensagens no console.

   ```python
   print("Olá, mundo!")
   ```

2. **`len()`**: Retorna o comprimento (número de itens) de uma lista, string, etc.

   ```python
   lista = [1, 2, 3]
   print(len(lista))  # Saída: 3
   ```

3. **`type()`**: Retorna o tipo de dado de uma variável.

   ```python
   numero = 42
   print(type(numero))  # Saída: <class 'int'>
   ```

4. **`int()`, `float()`, `str()`**: Convertem valores para inteiros, floats (números decimais) e strings (textos), respectivamente.

   ```python
   texto = "123"
   numero = int(texto)
   print(numero)  # Saída: 123
   ```

### Criando suas Próprias Funções

Além de usar funções internas, você pode criar suas próprias funções. Isso é útil quando você precisa de uma "receita" específica para sua tarefa.

#### Estrutura de uma Função

Para definir uma função, você usa a palavra-chave `def`, seguida pelo nome da função, parênteses (que podem conter parâmetros) e dois pontos. O código da função fica indentado.

```python
def saudacao():
    print("Olá, tudo bem?")
```

#### Chamando uma Função

Depois de definir uma função, você pode chamá-la pelo nome, seguido de parênteses.

```python
saudacao()  # Saída: Olá, tudo bem?
```

#### Funções com Parâmetros

Você pode passar informações para a função através de parâmetros.

```python
def saudacao(nome):
    print(f"Olá, {nome}, tudo bem?")

saudacao("João")  # Saída: Olá, João, tudo bem?
```

#### Funções com Retorno

Funções podem retornar valores usando a palavra-chave `return`.

```python
def soma(a, b):
    return a + b

resultado = soma(5, 3)
print(resultado)  # Saída: 8
```

### Resumo

- **Funções internas** são como ferramentas básicas que já vêm com o Python.
- **Funções definidas por você** são como receitas que você cria para realizar tarefas específicas.
- **Parâmetros** permitem que você passe informações para as funções.
- **Retorno** permite que a função envie um resultado de volta para onde foi chamada.

### Tabela de Funções Internas Comuns

| Função    | Descrição                                     |
| --------- | --------------------------------------------- |
| `print()` | Exibe uma mensagem ou valor no console        |
| `len()`   | Retorna o número de itens em um objeto        |
| `type()`  | Retorna o tipo de dado de uma variável        |
| `int()`   | Converte um valor para inteiro                |
| `float()` | Converte um valor para float (número decimal) |
| `str()`   | Converte um valor para string (texto)         |

Agora você tem uma compreensão básica sobre o que são funções, para que servem e como usá-las em Python!

