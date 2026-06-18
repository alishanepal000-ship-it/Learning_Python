# simple reflex agent: no memory, only reacts to current situation

# 4x4 grid: 'dirty' or 'clean'
grid = [
    ['dirty', 'clean', 'dirty', 'clean'],
    ['clean', 'dirty', 'clean', 'clean'],
    ['dirty', 'clean', 'dirty', 'dirty'],
    ['dirty', 'dirty', 'clean', 'dirty']
]

row, col = 0, 0  # start position
steps = 0

while not (row == 3 and col == 0):
    print(f'\nStep: {steps},  Position ({row},{col}), STATUS: {grid[row][col]}')
    # decision: only looks at current cell!
    if grid[row][col] == 'dirty':
        grid[row][col] = 'clean'
        print(f'  -> CLEAN AT f{(row, col)}')
    else:
        if row % 2 == 0:
            if col == 3:
                row +=1
                print(f'  -> MOVE FROM {(row - 1, col )} TO {(row, col)}')
            else:
                col += 1
                print(f'  -> MOVE FROM {(row, col - 1 )} TO {(row, col)}')
        else:
            if col == 0:
                row +=1
                print(f'  -> MOVE FROM {(row - 1, col )} TO {(row, col)}')
            else:
                col -= 1
                print(f'  -> MOVE FROM {(row, col + 1 )} TO {(row, col)}')

    steps += 1

if grid[row][col] == 'dirty':
    grid[row][col] = 'clean'
    print(f'  -> CLEAN AT f{(row, col)}')
    print(f'\ndone in {steps + 1} steps')
else:
    print(f'\ndone in {steps} steps')
