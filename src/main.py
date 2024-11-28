from Search import *
from Graph import graph


caminho_bfs = BFS(graph)
caminho_dfs = DFS(graph)


print(f" \n O caminho percorrido pelo BFS foi: {caminho_bfs}")
print(f" \n O caminho percorrido pelo DFS foi: {caminho_dfs}")