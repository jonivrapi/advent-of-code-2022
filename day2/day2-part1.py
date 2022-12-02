path = '/Users/jonivrapi/Documents/GitHub/advent-of-code-2022/day2/input.txt'

loss = 0
draw = 3
win = 6

rps = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

totalPoints = 0

with open(path) as input:
    contents = input.readlines()

for line in contents:
    [opponent, me] = line.split(' ')
    me = me.replace('\n', '')

    myPoints = rps.get(me)

    if (rps.get(opponent) == myPoints):
        totalPoints += (draw + myPoints)
    
    if (opponent == 'A' and me == 'Y'):
        totalPoints += (win + myPoints)
    
    if (opponent == 'A' and me == 'Z'):
        totalPoints += (loss + myPoints)
    
    if (opponent == 'B' and me == 'X'):
        totalPoints += (loss + myPoints)
    
    if (opponent == 'B' and me == 'Z'):
        totalPoints += (win + myPoints)
    
    if (opponent == 'C' and me == 'X'):
        totalPoints += (win + myPoints)
    
    if (opponent == 'C' and me == 'Y'):
        totalPoints += (loss + myPoints)

print(f'Total Points: {totalPoints}')
    