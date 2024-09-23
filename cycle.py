# Problem 9: Detect cycle in graph
def has_cycle(graph):
    visited = set()
    rec_stack = set()

    def visit(node):
        if node in rec_stack:
            return True
        if node in visited:
            return False

        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph[node]:
            if visit(neighbor):
                return True

        rec_stack.remove(node)
        return False

    return any(visit(node) for node in graph)

graph = {
    'A': {'B', 'C'},
    'B': {'C'},
    'C': {'A'},
    'D': {'E'},
    'E': set()
}

cycle_exists = has_cycle(graph)
print("Does the graph have a cycle?", cycle_exists)
