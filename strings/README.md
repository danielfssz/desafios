## Arquivos principais
A aplicação possui 3 arquivos. 'wrap.py' contém o método de quebra das strings, 'run.py' contém a chamada de execução da aplicação e 'test_wrap.py' contém a classe de testes.

## Outros arquivos
'README.md' contém este texto em formato markdown e 'Desafios.md' contém o processo de resolução deste desafio.

## Requisitos
É necessário ter o python na máquina para rodar o projeto. Caso esteja sendo usado Linux ou Mac, provavelmente já está instalado, caso não esteja, ou seja uma máquina Windows, é possível fazer o download no site oficial da linguagem: https://www.python.org/downloads/

## Comandos
Assumindo que o python está instalado e está no path do sistema, seguem os comandos para...

##### Executar a aplicação
```bash
python3 run.py
```
Primeiro é necessário passar o texto à ser formatado, em seguida o número máximo de colunas em que o mesmo terá e por fim, informar se o texto deverá estar justificado ou não.
O retorno da aplicação será o texto formatado com as configurações passadas no parâmetro.

##### Executar os testes
```bash
python3 -m unittest test_wrap.py
```

A classe de testes contém 7 métodos com as seguintes finalidades:
* Testar se o texto do input é uma variável do tipo string
* Testar se o número do input não é uma variável do tipo string
* Testar se o número do input não é uma variável de valor negativo
* Testar se o texto do input não está vazio
* Testar se o número do input não está vazio
* Testar se o número de caracteres por linha não é maior que o informado pelo usuário quando a flag de justificação é falsa
* Testar se o número de caracteres por linha é sempre igual ao número do input quando a flag de justificação é verdadeira