graph = {
    'A' : ['B', 'C'],
    'B' : ['F'],
    'C' : ['E', 'D'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = []
queue = ['A']

while queue:
    node = queue.pop(0)
    if node not in visited: 
        visited.append(node)
        neighbors = graph[node]
        print(neighbors)
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append(neighbor)

print(visited)
