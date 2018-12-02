## Dificuldades iniciais

* Pensar em uma lógica simples para justificar uma string.

## Passo a passo
O primeiro desafio foi resolvido rapidamente com o uso do método fill(text, number) do módulo textwrap, nativo do próprio python, que ao receber uma string e um valor inteiro, retorna uma lista com as strings quebradas de modo que seu tamanho não seja maior que o valor inteiro recebido e sem quebrar palavras ao meio.
Com o primeiro desafio recebido, foi necessário desenvolver um algoritmo que justificasse as strings de forma a ter sempre o mesmo tamanho do valor inteiro recebido, e a lógica foi a seguinte:
Há um contador de espaços em branco e um registrador, enquanto a string for menor que o valor inteiro recebido, o algoritmo procura o primeiro espaço em branco e compara com o registrador, se o contador for maior que o registrador (o espaço atual vem depois do último), é adicionado um espaço em branco, se não for, procura o próximo espaço em branco e executa o mesmo algoritmo. Quando o registrador é igual ao número de espaços em branco na string (não há um próximo espaço em branco), o mesmo é zerado de forma que o loop se reinicie. Com isso a string ganha caracteres vazios de forma distribuída entre os espaços pré-existentes de forma que fique do tamanho do valor inteiro recebido gerando uma lista de strings justificadas.
O arquivo 'run.py' foi criado para executar a aplicação via CLI e os testes unitários foram desenvolvidos de forma a testar possíveis variações nos inputs.