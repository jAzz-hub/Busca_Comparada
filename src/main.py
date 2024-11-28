from Search import *
from Graph import graph
from Measurements import measure_algorithm

caminho_bfs, tempo_bfs, memoria_bfs_atual, memoria_bfs_pico = measure_algorithm(BFS, graph)
caminho_dfs, tempo_dfs, memoria_dfs_atual, memoria_dfs_pico = measure_algorithm(DFS, graph)

total_memory_bfs  = memoria_bfs_atual / 1024 
peak_memory_bfs   = memoria_bfs_pico / 1024 

total_memory_dfs  = memoria_dfs_atual / 1024
peak_memory_dfs   = memoria_dfs_pico / 1024

print(f" \n O caminho percorrido pelo BFS foi: {caminho_bfs}")
print(f"Tempo de execução do BFS: {tempo_bfs:.6f} segundos")
print(f"Memória utilizada pelo BFS: {total_memory_bfs} KB (atual), {peak_memory_bfs} KB (pico)")

print(f" \n O caminho percorrido pelo DFS foi: {caminho_dfs}")
print(f"Tempo de execução do DFS: {tempo_dfs:.6f} segundos")
print(f"Memória utilizada pelo DFS: {total_memory_dfs} KB (atual), {peak_memory_dfs} KB (pico)")

