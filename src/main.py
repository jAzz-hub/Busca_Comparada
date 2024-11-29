import math
from Search import *
from Graph import graph
from Measurements import measure_algorithm

def calcular_desvio_padrao(valores, media, num_execucoes):
    diffs_quadrados = [(valor - media) ** 2 for valor in valores]
    variancia = sum(diffs_quadrados) / num_execucoes
    return math.sqrt(variancia)

def medir_multiple_execucoes(algoritmo, grafo, num_execucoes=5):
    tempos = []
    memoria_atual = []
    memoria_pico = []

    for _ in range(num_execucoes):
        tempo, memoria_atual_exec, memoria_pico_exec = measure_algorithm(algoritmo, grafo)
        tempos.append(tempo)
        memoria_atual.append(memoria_atual_exec)
        memoria_pico.append(memoria_pico_exec)

    # Calcular a média
    avg_tempo = sum(tempos) / num_execucoes
    avg_memoria_atual = sum(memoria_atual) / num_execucoes / 1024  # Converter para KB
    avg_memoria_pico = sum(memoria_pico) / num_execucoes / 1024  # Converter para KB

    # Calcular o desvio padrão
    std_tempo = calcular_desvio_padrao(tempos, avg_tempo, num_execucoes)
    std_memoria_atual = calcular_desvio_padrao(memoria_atual, avg_memoria_atual * 1024, num_execucoes) / 1024  
    std_memoria_pico = calcular_desvio_padrao(memoria_pico, avg_memoria_pico * 1024, num_execucoes) / 1024  

    return avg_tempo, avg_memoria_atual, avg_memoria_pico, std_tempo, std_memoria_atual, std_memoria_pico

def imprimir_desempenho(nome_algoritmo, avg_tempo, avg_memoria_atual, avg_memoria_pico, std_tempo, std_memoria_atual, std_memoria_pico):
    print(f"\nDesempenho do {nome_algoritmo}:")
    print(f"Tempo de execução médio: {avg_tempo:.6f} segundos (Desvio padrão: {std_tempo:.6f})")
    print(f"Memória utilizada média: {avg_memoria_atual:.2f} KB (atual), {avg_memoria_pico:.2f} KB (pico) ")

num_execucoes = 100

tempo_bfs, memoria_bfs_atual, memoria_bfs_pico, std_tempo_bfs, std_mem_bfs_atual, std_mem_bfs_pico = medir_multiple_execucoes(BFS, graph, num_execucoes)
tempo_dfs, memoria_dfs_atual, memoria_dfs_pico, std_tempo_dfs, std_mem_dfs_atual, std_mem_dfs_pico = medir_multiple_execucoes(DFS, graph, num_execucoes)

imprimir_desempenho("BFS", tempo_bfs, memoria_bfs_atual, memoria_bfs_pico, std_tempo_bfs, std_mem_bfs_atual, std_mem_bfs_pico)
imprimir_desempenho("DFS", tempo_dfs, memoria_dfs_atual, memoria_dfs_pico, std_tempo_dfs, std_mem_dfs_atual, std_mem_dfs_pico)
