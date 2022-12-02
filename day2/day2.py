path = '/Users/jonivrapi/Documents/GitHub/advent-of-code-2022/day2/input.txt';

totals = []

with open(path) as input:
    contents = input.readlines()
    
    tempTotal = 0

for line in contents:
    if (line == '\n'):
        totals.append(tempTotal)
        tempTotal = 0
    else:
        tempTotal += int(line)

totals.sort(reverse=True)
maxTotal = totals[0] + totals[1] + totals[2]

print(f'Max Total: {maxTotal}')
