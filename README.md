# Projeto de Algoritmos

Este projeto visa implementar diversos algoritmos para resolver problemas de busca, criptografia, palíndromos e anagramas.

## Índice

- [Visão Geral](#visão-geral)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Contato](#contato)

## Visão Geral

O projeto consiste na implementação de algoritmos para resolver problemas específicos: determinar o horário com maior número de estudantes acessando uma plataforma educacional, testar uma função de criptografia, verificar se uma palavra é um palíndromo, comparar strings para identificar anagramas, e encontrar números duplicados em um array. Cada problema é abordado com diferentes estratégias algorítmicas, incluindo busca, recursividade e ordenação.

## Tecnologias Utilizadas

- Python
- Bibliotecas de Teste: `pytest`

## Instalação

Para instalar e executar este projeto localmente, siga as instruções abaixo:

1. Clone o repositório:
    ```sh
    git clone git@github.com:matheusrosa1/project_algorithms.git
    cd project_algorithms
    ```

2. Crie um ambiente virtual:
    ```sh
    python -m venv venv
    ```

3. Ative o ambiente virtual:
    - No Windows:
        ```sh
        venv\Scripts\activate
        ```
    - No macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Como Usar

Após a instalação, você pode utilizar as seguintes funcionalidades do projeto:

### Determinar o Horário com Maior Número de Estudantes

1. Implemente a função no arquivo `challenges/challenge_study_schedule.py`.
2. Para usar a função, execute:
    ```python
    from challenges.challenge_study_schedule import study_schedule

    periods = [(1, 4), (2, 5), (7, 8)]
    target_time = 3
    result = study_schedule(periods, target_time)
    print(result)  # Exibe o número de estudantes no horário alvo
    ```

### Verificar se uma Palavra é um Palíndromo (Recursivo)

1. Implemente a função no arquivo `challenges/challenge_palindromes_recursive.py`.
2. Para usar a função, execute:
    ```python
    from challenges.challenge_palindromes_recursive import is_palindrome_recursive

    result = is_palindrome_recursive("radar", 0, len("radar") - 1)
    print(result)  # True
    ```

### Verificar se uma Palavra é um Palíndromo (Iterativo)

1. Implemente a função no arquivo `challenges/challenge_palindromes_iterative.py`.
2. Para usar a função, execute:
    ```python
    from challenges.challenge_palindromes_iterative import is_palindrome_iterative

    result = is_palindrome_iterative("radar")
    print(result)  # True
    ```

### Comparar Strings para Identificar Anagramas

1. Implemente a função no arquivo `challenges/challenge_anagrams.py`.
2. Para usar a função, execute:
    ```python
    from challenges.challenge_anagrams import are_anagrams

    result = are_anagrams("Listen", "Silent")
    print(result)  # (sorted string1, sorted string2, True)
    ```

### Encontrar Números Duplicados em um Array

1. Implemente a função no arquivo `challenges/challenge_find_the_duplicate.py`.
2. Para usar a função, execute:
    ```python
    from challenges.challenge_find_the_duplicate import find_duplicate

    nums = [1, 3, 4, 2, 2]
    result = find_duplicate(nums)
    print(result)  # Exibe o número duplicado
    ```

## Contribuição

Para contribuir com o projeto, siga os passos abaixo:

1. Fork o repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Crie um novo Pull Request.

## Licença

Licença [MIT](https://github.com/matheusrosa1/project_algorithms?tab=MIT-1-ov-file) 

## Contato

Para mais informações, entre em contato com os mantenedores do projeto:

- GitHub: [matheusrosa1](https://github.com/matheusrosa1/)
- E-mail: matheusrosataxa@gmail.com
