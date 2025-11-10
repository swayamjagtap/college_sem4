from collections import deque

#with sets--------------------
graph1 = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}
def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
    return visited
visited = dfs(graph1, 'A', [])
print(visited) 

#without sets--------------------
graph2 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
def dfs_no_set(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            dfs_no_set(graph, neighbor, visited)
    return visited
visited_no_set = dfs_no_set(graph2, 'A', [])
print(visited_no_set)  # Output: ['A', 'B', 'D', 'E', 'F', 'C']