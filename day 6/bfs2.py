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

path = {'A' : ['A']}

#destination = 'C'

while queue:
    node = queue.pop(0)
    if node not in visited:
        visited.append(node)
        neighbors = graph[node]
        for neighbor in neighbors:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
                #print(path[neighbor])
                path[neighbor] = path[node] + [neighbor]
                print(path[neighbor])


    