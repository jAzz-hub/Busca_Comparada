## Descrição do Projeto

Este projeto implementa e compara dois algoritmos de busca não informada aplicados ao **problema do labirinto**. O objetivo é testar a eficiência de diferentes técnicas de busca em um ambiente clássico de busca em grafos. O labirinto é representado por um arquivo de entrada (CSV ou Excel) contendo o mapa do labirinto, e o objetivo do algoritmo é encontrar o caminho mais curto entre o ponto inicial e o ponto de destino.

## Objetivos

- Implementar dois algoritmos de busca não informada:
  - **Busca em Largura (BFS)**
  - **Busca em Profundidade (DFS)**
- Comparar os algoritmos em termos de:
  - **Tempo de execução**: Quanto tempo cada algoritmo leva para encontrar a solução.
  - **Uso de memória**: A quantidade de memória utilizada durante a execução dos algoritmos.
  - **Completude**: Verificar se o algoritmo encontra uma solução sempre que ela existir.
  - **Optimalidade**: Determinar se o caminho encontrado é o mais curto.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:
```
.
├── data                        # Arquivos de entrada (labirinto em formatos CSV e Excel)
│   ├── Maze.csv                # Mapa do labirinto em formato CSV
├── EC_IA_Trabalho_01_1.pdf     # Documento PDF com as instruções do trabalho
├── Graph.txt                   # Representação do labirinto em formato de texto
├── Labirínto_corrigido.PNG     # Imagem do labirinto para visualização
├── README.md                   # Este arquivo
└── src
    ├── Graph.py                # Implementação da representação do grafo (labirinto)
    ├── main.py                 # Arquivo principal para execução dos algoritmos
    ├── Measurements.py         # Funções para medições de desempenho
    ├── Search.py               # Implementação dos algoritmos de busca (BFS e DFS)
```
## Instruções de Execução

1. **Instalar as dependências**: 
   - Se necessário, instale as dependências do projeto com o comando:

     ```bash
     pip install pandas
     ```

2. **Rodar o projeto**:
   - Para rodar o programa, execute o seguinte comando no terminal:

     ```bash
     python src/main.py
     ```

   Isso irá iniciar a execução dos dois algoritmos (BFS e DFS) e imprimir a média seu tempo de execução, aplicar as buscas no labirinto e gerar as medições de desempenho.

## Arquivos Importantes

- **`data/Maze.csv`: Arquivos que contêm o mapa do labirinto em formato CSV. O mapa é lido pelo programa para a execução dos algoritmos.
- **`src/Graph.py`**: Contém a implementação para representar o labirinto como um grafo e manipular o mapa do labirinto.
- **`src/Search.py`**: Contém a implementação dos algoritmos de busca (BFS e DFS).
- **`src/Measurements.py`**: Fornece funções para medir o desempenho dos algoritmos, incluindo tempo de execução e uso de memória.

## Contribuições

Este projeto foi realizado como parte da disciplina de Inteligência Artificial do curso de Engenharia de Computação do **CEFET-MG - Campus Divinópolis**, sob a orientação do Prof. Tiago Alves de Oliveira. O trabalho foi desenvolvido por:
- **[Getúlio Santos Mende](https://github.com/Getulio-Mendes)**.
- **[João Gustavo Silva Guimarães](https://github.com/jAzz-hub)**.
- **[oão Pedro Freitas de Paula](https://github.com/joaopedrofreitas)**

