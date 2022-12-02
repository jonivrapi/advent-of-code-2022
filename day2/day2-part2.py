path = '/Users/jonivrapi/Documents/GitHub/advent-of-code-2022/day2/input.txt'

loss = 0
draw = 3
win = 6

rock = 1
paper = 2
scissors = 3

totalPoints = 0

with open(path) as input:
    contents = input.readlines()

for line in contents:
    [opponent, me] = line.split(' ')
    me = me.replace('\n', '')

    if me == 'X':
        if opponent == 'A':
            totalPoints += (loss + scissors)
        if opponent == 'B':
            totalPoints += (loss + rock)
        if opponent == 'C':
            totalPoints += (loss + paper)

    if me == 'Y':
        if opponent == 'A':
            totalPoints += (draw + rock)
        if opponent == 'B':
            totalPoints += (draw + paper)
        if opponent == 'C':
            totalPoints += (draw + scissors)

    if me == 'Z':
        if opponent == 'A':
            totalPoints += (win + paper)
        if opponent == 'B':
            totalPoints += (win + scissors)
        if opponent == 'C':
            totalPoints += (win + rock)

print(f'Total Points: {totalPoints}')
    