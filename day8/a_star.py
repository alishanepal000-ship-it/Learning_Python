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

# tracks the actual cost from starting to current node, does not consider heuristic cost
total_cost = {start: 0} 
parent = {}

while open_list:
    current = open_list[0]
    for node in open_list:
        if total_cost[node] + heuristic[node] < total_cost[current] + heuristic[current]:
            current = node

    open_list.remove(current)
    closed.append(current)

    if current == goal:
        break

    for neighbor, cost in graph[current]:
        new_g = total_cost[current] + cost

        if neighbor not in total_cost:
            total_cost[neighbor] = new_g
            parent[neighbor] = current
            open_list.append(neighbor)

        elif new_g < total_cost[neighbor]:
            total_cost[neighbor] = new_g
            parent[neighbor] = current

            if neighbor in closed:
                closed.remove(neighbor)
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

print("A* Path:", path)
print("Total Cost:", total_path_cost,total_cost)


