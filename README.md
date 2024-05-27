# Título do Projeto

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
- Bibliotecas de Teste: unittest


## Instalação

Clone o repositório

* Use o comando: `git clone git@github.com:matheusrosa1/project_algorithms.git`.
* Entre na pasta do repositório que você acabou de clonar:
  * `cd sd-035-project-algorithms`

  2. Crie o ambiente virtual para o projeto

* `python3 -m venv .venv && source .venv/bin/activate`

  3. Instale as dependências

* `python3 -m pip install -r dev-requirements.txt`

## Como Usar

Após a instalação, você pode utilizar as seguintes funcionalidades do projeto:

Determinar o Horário com Maior Número de Estudantes
Implemente a função no arquivo challenges/challenge_study_schedule.py.
Para usar a função, execute:
python
Copiar código
from challenges.challenge_study_schedule import study_schedule

periods = [(1, 4), (2, 5), (7, 8)]
target_time = 3
result = study_schedule(periods, target_time)
print(result)  # Exibe o número de estudantes no horário alvo
Testar a Função de Criptografia
Implemente os testes no arquivo tests/encrypt/test_encrypt.py.
Para executar os testes, use:
sh
Copiar código
python -m unittest discover -s tests/encrypt
Verificar se uma Palavra é um Palíndromo (Recursivo)
Implemente a função no arquivo challenges/challenge_palindromes_recursive.py.
Para usar a função, execute:
python
Copiar código
from challenges.challenge_palindromes_recursive import is_palindrome_recursive

result = is_palindrome_recursive("radar")
print(result)  # True
Comparar Strings para Identificar Anagramas
Implemente a função no arquivo challenges/challenge_anagrams.py.
Para usar a função, execute:
python
Copiar código
from challenges.challenge_anagrams import are_anagrams

result = are_anagrams("Listen", "Silent")
print(result)  # (sorted string1, sorted string2, True)


## Contribuição

Para contribuir com o projeto, siga os passos abaixo:

1. Fork o repositório.
2. Crie uma branch para sua feature (git checkout -b feature/nova-feature).
3. Commit suas mudanças (git commit -am 'Adiciona nova feature').
4. Push para a branch (git push origin feature/nova-feature).
5. Crie um novo Pull Request.


## Licença

Declare a licença do projeto. Se você está utilizando uma licença padrão (por exemplo, MIT, Apache), inclua o texto da licença no README. Se estiver utilizando uma licença personalizada, forneça informações sobre ela.

## Contato

GitHub: https://github.com/matheusrosa1
E-mail: matheusrosataxa@gmail.com
