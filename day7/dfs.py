graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start = 'A'
visited = []
stack = [start]
path = {'A': ['A']}

while stack:
    print(f'\nStack before pop: {stack}')
    node = stack.pop()
    print(f'Popped: {node}')

    if node not in visited:
        visited.append(node)
        print(f'Visited: {visited}')

        # for neighbor in graph[node]:
        for neighbor in reversed(graph[node]):
            if neighbor not  in visited and neighbor not in stack:
                stack.append(neighbor)
                print(f'Added {neighbor} to stack')
                path[neighbor] = path[node] + [neighbor]
    
    print(f'Stack after: {stack}')

print(f'\nFinal visited order: {visited}')
print(path)
