# Problem 8: DFS traversal for reachable nodes
def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node] - visited)
    return visited

graph = {
    'A': {'B', 'C'},
    'B': {'D'},
    'C': {'D'},
    'D': {'E'},
    'E': set()
}

reachable_nodes = dfs(graph, 'A')
print("Nodes reachable from A:", reachable_nodes)
