
#Sujestão para modelagem e leitura do grafo

from pandas import read_csv

Alphabet = {
    'A' : 0,
    'B' : 1,
    'C' : 2,
    'D' : 3,
    'E' : 4,
    'F' : 5,
    'G' : 6,
    'H' : 7,
    'I' : 8,
    'J' : 9,
    'K' : 10,
    'L' : 11,
    'M' : 12,
    'N' : 13,
    'O' : 14,
    'P' : 15,
    'Q' : 16,
    'R' : 17,
    'S' : 18,
    'T' : 19,
    'U' : 20,
    'V' : 21,
    'X' : 22,
    'Y' : 23,
    'Z' : 24
 }



def Graph():    #Consumindo o grafo em csv e retornando em matriz
    graph = read_csv('../data/Maze.csv')  #Consumindo csv
    graph.drop(['Unnamed: 0'], axis=1, inplace=True)
    return graph.to_numpy()



graph = Graph()

print(graph)

print(graph[Alphabet['A']][Alphabet['F']])      # Verificando se existe uma aresta entre 2 vértices
