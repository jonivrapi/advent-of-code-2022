path = '/Users/jonivrapi/Documents/GitHub/advent-of-code-2022/day1/input.txt'

maxTotal = 0

with open(path) as input:
    contents = input.readlines()
    
    tempTotal = 0

for line in contents:
    if (line == '\n'):
        if (maxTotal < tempTotal):
            maxTotal = tempTotal
        
        tempTotal = 0
    else:
        tempTotal += int(line)

    
print(f'Max Total: {maxTotal}')
