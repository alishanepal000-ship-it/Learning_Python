# utiltiy based agent: Chooses action with highest numerical score

grid = [
    ['dirty', 'clean', 'dirty', 'clean'],
    ['clean', 'dirty', 'clean', 'clean'],
    ['dirty', 'clean', 'dirty', 'dirty'],
    ['clean', 'clean', 'clean', 'dirty']
]

def utility(action, row, col, battery):
    '''calculate score for each possible action'''
    score = 0

    # +100 for cleaning dirt
    if action == 'CLEAN' and grid[row][col] == 'dirty':
        score += 100

    # -10 for moving (uses energy)
    if action in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
        score -= 10

    # -50 if battery is low (emergency)
    if battery < 20:
        score -= 50

    # -20 for trying to move into wall
    if action == 'RIGHT' and col == 3:
        score -= 20
    if action == 'LEFT' and col == 0:
        score -= 20
    if action == 'DOWN' and row == 3:
        score -= 20
    if action == 'UP' and row == 0:
        score -= 20

    return score

# Run the agent
row, col = 0, 0
battery = 100
steps = 0
actions = ['CLEAN', 'RIGHT', 'LEFT', 'DOWN', 'UP']

while steps < 25 and battery > 0:
    # try all actions, pick the best utility
    best_action = None
    best_score = -9999

    for act in actions:
        score = utility(act, row, col, battery)
        if score > best_score:
            best_score = score
            best_action = act

    print(f'({row},{col}): {grid[row][col]} → chose {best_action} (score={best_score})')

    # execute action
    if best_action == 'CLEAN' and grid[row][col] == 'dirty':
        grid[row][col] = 'clean'
        battery -= 2
    elif best_action == 'RIGHT' and col < 3:
        col += 1
        battery -= 5
    elif best_action == 'LEFT' and col > 0:
        col -= 1
        battery -= 5
    elif best_action == 'DOWN' and row < 3:
        row += 1
        battery -= 5
    elif best_action == 'UP' and row > 0:
        row -= 1
        battery -= 5

    steps += 1
    print(f'  Battery: {battery}%')

print(f'\ndone in {steps} steps')
