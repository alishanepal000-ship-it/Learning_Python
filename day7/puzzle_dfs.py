start = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# DFS with visited tracking
stack = [start]          # Stack instead of Queue (LIFO)
paths = [[]]
visited = [str(start)]
state_count = 0

print(f'Start: {start}')
print(f'Goal:  {goal}')
print('\nSearching...\n')

while stack:
    # Pop from end (LIFO - Depth First)
    state = stack.pop()
    path = paths.pop()
    state_count += 1

    # Show progress
    if state_count % 100 == 0:
        print(f'  Progress: {state_count} states explored, Stack size: {len(stack)}')

    # Check goal
    if state == goal:
        print('SOLUTION FOUND!')
        print(f'  Moves: {len(path)}')
        print(f'  Path: {' -> '.join(path)}')
        print(f'  States explored: {state_count}')
        print(f'  States in visited set: {len(visited)}')
        print(f'  States still in stack: {len(stack)}')
        break

    # Find blank
    br = bc = -1 # br = blank row, bc = blank column
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                br, bc = i, j

    # Generate moves
    move_options = [(-1,0,'UP'), (1,0,'DOWN'), (0,-1,'LEFT'), (0,1,'RIGHT')]

    for dr, dc, move_name in move_options:
        nr, nc = br + dr, bc + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            new_state = [row[:] for row in state]
            new_state[br][bc], new_state[nr][nc] = new_state[nr][nc], new_state[br][bc]

            state_key = str(new_state)

            # VISITED CHECK - Prevents revisiting states
            if state_key not in visited:
                visited.append(state_key)
                stack.append(new_state)
                paths.append(path + [move_name])

                # Show progress
                if len(visited) % 20 == 0:
                    print(f'  Progress: {len(visited)} states visited, {len(stack)} in stack')
            # else: State already visited, skip it

print('STATISTICS:')
print(f'  Total unique states visited: {len(visited)}')
print(f'  States that were skipped (already visited): {state_count - len(visited)}')
print(f'  Final stack size: {len(stack)}')
