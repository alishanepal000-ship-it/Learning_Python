# goal based agent: creates a complete plan before acting

grid = [
    ['dirty', 'clean', 'dirty', 'clean'],
    ['clean', 'dirty', 'clean', 'clean'],
    ['dirty', 'clean', 'dirty', 'dirty'],
    ['clean', 'clean', 'clean', 'dirty']
]

# step 1: find all dirty cells (the GOAL)
dirty_cells = []
for r in range(4):
    for c in range(4):
        if grid[r][c] == 'dirty':
            dirty_cells.append((r, c))

print(f'Goal: Clean {len(dirty_cells)} cells at {dirty_cells}')

# step 2: create a plan (path to each dirty cell)
plan = []
row, col = 0, 0  # start


for target_r, target_c in sorted(dirty_cells):  # sorted for simple path
    # add moves to reach target
    while col < target_c:
        plan.append('RIGHT')
        col += 1
    while col > target_c:
        plan.append('LEFT')
        col -= 1
    while row < target_r:
        plan.append('DOWN')
        row += 1
    while row > target_r:
        plan.append('UP')
        row -= 1
    plan.append('CLEAN')

print(f'Plan: {plan}')

# step 3: execute the plan
row, col = 0, 0
for action in plan:
    if action == 'RIGHT':
        col += 1
        print(f'MOVE {action} from {(row, col-1)} TO {(row, col)}')
    elif action == 'LEFT':
        col -= 1
        print(f'MOVE {action} from {(row, col+1)} TO {(row, col)}')
    elif action == 'DOWN':
        row += 1
        print(f'MOVE {action} from {(row-1, col)} TO {(row, col)}')
    elif action == 'UP':
        row -= 1
        print(f'MOVE {action} from {(row+1, col)} TO {(row, col)}')
    else:
        grid[row][col] = 'clean'
        print(f'CLEAN {(row, col)}')

print(grid)
print(f'\ncompleted in {len(plan)} actions')
