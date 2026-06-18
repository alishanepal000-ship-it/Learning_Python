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

iteration = int(input('Enter maximum no. of steps: '))


moves = {
    'l': 'LEFT',
    'r': 'RIGHT',
    'u': 'UP',
    'd': 'DOWN'
}

while steps < iteration:
    print(f'\nStep: {steps},  Position ({row},{col}), STATUS: {grid[row][col]}')
    # decision: only looks at current cell!
    if grid[row][col] == 'dirty':
        grid[row][col] = 'clean'
        print(f'  -> CLEAN AT f{(row, col)}')
    else:
        possible_moves = []

        if col == 0:
            possible_moves.append('RIGHT')
        elif col == 3:
            possible_moves.append('LEFT')
        else:
            possible_moves.append(*['LEFT, RIGHT'])
        if row == 0:
            possible_moves.append('DOWN')
        elif row == 3:
            possible_moves.append('UP')
        else:
            possible_moves.append(*['UP, DOWN'])

        for move in possible_moves:
            print(f'  -> PRESS {move[0].lower()} to move {move}')

        usr_input = input('  -> ENTER YOUR VALUE: ')

        if usr_input == 'l':
            col -= 1
        elif usr_input == 'r':
            col += 1
        elif usr_input == 'u':
            row -= 1
        elif usr_input == 'd':
            row += 1
        else:
            pass
        print(f'  -> MOVE FROM {(row, col)} TO {row, col}')


    steps += 1


print(f'\ndone in {steps + 1} steps')