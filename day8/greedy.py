graph = {
    'S': [('A', 2), ('B', 3)],
    
    'A': [('C', 2), ('D', 4)],
    'B': [('E', 1), ('F', 5)],
    
    'C': [('H', 1), ('I', 8)],
    'D': [('J', 2)],
    'E': [('K', 10)],
    'F': [('L', 1)],
    
    'H': [('M', 1)],           
    'I': [('N', 2)],
    'J': [('N', 1)],
    'K': [('O', 1)],
    'L': [('O', 2)],
    
    'M': [('G', 25)],          
    'N': [('G', 2)],
    'O': [('G', 2)],
    'G': []
}

heuristic = {
    'S': 12,
    
    'A': 9,
    'B': 10,
    
    'C': 6,                  
    'D': 8,
    'E': 9,
    'F': 8,
    
    'H': 3,                  
    'I': 5,
    'J': 4,
    'K': 3,
    'L': 4,
    
    'M': 1,                  
    'N': 2,
    'O': 2,
    'G': 0
}

start = 'S'
goal = 'G'

open_list = [start]
closed = []

parent = {}

while open_list:

    # find node with minimum f = h
    current = open_list[0]

    for node in open_list:
        if heuristic[node] < heuristic[current]:
            current = node

    open_list.remove(current)
    closed.append(current)

    if current == goal:
        break

    for neighbor, cost in graph[current]:

        if neighbor not in open_list and neighbor not in closed:
            parent[neighbor] = current
            open_list.append(neighbor)

path = []
node = goal

while node != start:
    path.append(node)
    node = parent[node]

path.append(start)
path.reverse()

total_path_cost = 0
for i in range(len(path) - 1):
    current_node = path[i]
    next_node = path[i+1]
    for neighbor, edge_cost in graph[current_node]:
        if neighbor == next_node:
            total_path_cost += edge_cost
            break

print("Greedy Best-First Path:", path)
print("Total Cost:", total_path_cost)