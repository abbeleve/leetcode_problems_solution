def find_cycle(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
    
    color = [0] * n
    parent = [-1] * n
    cycle_path = []

    def dfs():
        