# arvoreBinaria-PYTHON-2023.1
# ESTRUTURA DE DADOS 
Código de Árvore Binária em Python realizado em aula, juntamente ao professor @marceloarantes19.

# BUSCA EM VETORES
- Algoritmos que buscam dados de um vetor são construídos em uma função que retorna o índice de um vetor. Se o valor encontrado é -1, o valor procurado não está no vetor.

**1. Busca Sequencial**
- É uma função que recebe o vetor e o valor a serem procurados no vetor, utilizando um laçõ de repetição que possui uma variável de controle (i) que passa por todos os valores válidos
#

**2. Busca Binária**
- É uma função que busca o elemento central. Se o elemento central for o que buscamos, retornamos o índice. Se não, dividimos o vetor em limite superior e inferior, andando pelo vetor.
**ATENÇÃO: Para executar a Busca Binária, o vetor deve estar em ordem crescente**
#

**CONSIDERAÇÕES FINAIS**
- A Busca Binária é a melhor opção, pois a sua complexidade de tempo é _O(log2n)_. Já a Busca Sequencial é _O(n)_
- A complexidade de espaço é dada pelo tamanho do vetor, ou seja, _O(n)_.
  
***Caso não encontre, é necessário uma condição, onde o programa deve retornar -1***
