from collections import deque

#with set()----------
graph1 = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}

def bfs(graph, start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node]-set(visited))
    return visited
print(bfs(graph1, 'A'))

#without set()----------
graph2 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
def bfs_no_set(graph, start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for neighbor in sorted(graph[node]):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    return visited
print(bfs_no_set(graph2, 'A')) 
# Output: ['A', 'B', 'C', 'D', 'E', 'F']