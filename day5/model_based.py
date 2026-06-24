# model based agent: has memory of which cells are clean

grid = [
    ['dirty', 'clean', 'dirty', 'clean'],
    ['clean', 'dirty', 'clean', 'clean'],
    ['dirty', 'clean', 'dirty', 'dirty'],
    ['clean', 'clean', 'clean', 'dirty']
]

# memory: True = we know this cell is clean
memory = [[False]*4 for _ in range(4)]
any_dirty = any(False in row for row in memory)

row, col = 0, 0
steps = 0

usr_input = 'y'

# while steps < 30:
while usr_input != 'n' and any_dirty:
    print(f'STEP: {steps}, POSITION ({row},{col}): {grid[row][col]}')

    # decision: clean if dirty, else find unknown cell
    if grid[row][col] == 'dirty':
        grid[row][col] = 'clean'
        # update memory
        memory[row][col] = True
        print(f'CELL {(row, col)} CLEANED')
    else:
        # update memory
        memory[row][col] = True
        print(f'Cell {(row, col)} is CLEAN, MOVE FORWARD')
        # find first cell we don't know about
        found = False
        for target_row in range(4):
            for target_col in range(4):
                is_clean = memory[target_row][target_col]
                if not is_clean:
                    # move toward target
                    if col < target_col:
                        col += 1
                    elif col > target_col:
                        col -= 1
                    elif row < target_row:
                        row += 1
                    elif row < target_row:
                        row -= 1
                    found = True
                    break
                else:
                    memory[target_row][target_col] = True
            if found:
                break
        print(f'  -> MOVED TO {(row, col)}')
    any_dirty = any(False in row for row in memory)
    usr_input = input('GO forward: ')
    steps += 1

print(f'\ndone in {steps} steps')
