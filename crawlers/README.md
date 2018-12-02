## Arquivos principais
A aplicação possui 4 arquivos principais. 'crawler.py' contém as funções de scrapping das páginas do reddit, 'run.py' contém a chamada de execução da aplicação via CLI, 'telegram_bot.py' contém as instruções para o bot do telegram e 'test_crawler.py' contém a classe de testes.

## Outros arquivos
'README.md' contém este texto em formato markdown, 'invalid_mock_html.html' e 'mock_html.html' contém exemplos de páginas mockadas para os testes unitários, 'requirements.txt' contém a lista dos pacotes necessários para a execução desta aplicação, 'dockerfile' contém as instruções à serem enviadas ao docker no momento de buildar o container e 'Desafios.md' contém o processo de resolução 

## Requisitos
É necessário ter o python na máquina para rodar o projeto. Caso esteja sendo usado Linux ou Mac, provavelmente já está instalado, caso não esteja, ou seja uma máquina Windows, é possível fazer o download no site oficial da linguagem: https://www.python.org/downloads/
É necessário também utilizar o pip (gerenciador de pacotes python) para a instalação das dependências que pode ser instalado através das instruções do site: https://pip.pypa.io/en/stable/installing/.
Após a instalação do python é necessário instalar via pip os requisitos através seguinte do comando:
```bash
pip install requirements.txt
```

## Bot
O bot utilizado nesta aplicação chama-se *OldRedditCrawler*, é possível encontrá-lo dentro do telegram no campo de busca. Ao informar ao bot o comando /nadaparafazer seguido de uma lista de subreddits, o bot retornara depois de alguns segundos as informações.
Exemplo:
```bash
/nadaparafazer worldnews;soccer;europe
```

## Comandos
Assumindo que os requisitos foram cumpridos, seguem os comandos para...

#### Executar a aplicação via CLI
```bash
python3 run.py
```
Após a exibição da mensagem passa-se como parâmetro uma lista de subreddits, por exemplo:
```bash
worldnews;soccer;europe
```

#### Executar o bot do telegram localmente
```bash
python3 telegram_bot.py
```

#### Executar os testes
```bash
python3 -m unittest test_crawler.py 
```

A classe de testes contém 4 métodos com as seguintes finalidades:
* Testar se as informações corretas das threads estão sendo retornadas
* Testar se a mensagem de erro correta é enviada quando uma thread é inválida
* Testar se o input da lista de threads está vazio
* Testar se há algum caractere inválido em algum elemento da lista de threads

## Docker
Para executar a aplicação via docker não são necessárias as instalações mencionadas no tópico 'requisitos', porém, é necessário a instalação e configuração do mesmo na máquina. O download pode ser feito através do site oficial 'https://www.docker.com/products/docker-desktop'.
Com o docker instalado, é feita a criação do container através do seguinte comando:
```bash
docker build -t nome_do_container .
```
Lembrando que é necessário estar no mesmo diretório do arquivo dockerfile, caso contrário, no lugar do . é necessário passar seu caminho.
Após a criação do container, pode-se obter seu ID através do seguinte comando:
```bash
docker images
```
Com o ID, é possível executá-lo através do seguinte comando:
```bash
docker run -it ID
```