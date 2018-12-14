INPUT = 50000000000

transformations = {}
state = None

with open('subterranean-sustainability-input.txt', 'r') as file:
    state = file.readline()[15:].strip()
    file.readline() # waste an empty line
    for line in file:
        line = line.strip()
        plants_from = line[:line.find('=')-1]
        plants_to = line[-1]
        transformations[plants_from] = plants_to

def get_nearby_plants(state, index):
    k = ''
    for i in range(index-2, index+3):
        if i < 0 or i >= len(state):
            k += '.'
        else:
            k += state[i]
    return k

def generation_step(state, transformations):
    new = ''
    
    for i in range(-2, len(state)+2):
        k = get_nearby_plants(state, i)
        if k in transformations:
            new += transformations[k]
        else:
            new += '.'
    
    return new

def see_pattern():
    '''
        To solve this problem a pattern appears after the 195th
        generation: the sum is just +53 every generation after.
        This piece of code shows this happening
    '''
    start = 0
    prev = 0
    for i in range(250):
        state = generation_step(state, transformations)
        start += 2
        total = 0
        for k in range(0, len(state)):
            if state[k] == '#':
                total += k - start
        print(i, ":", total, "\tdifference:", abs(total - prev))
        prev = total

start = 0
for _ in range(195):
    state = generation_step(state, transformations)
    start += 2

total = 0
for k in range(0, len(state)):
    if state[k] == '#':
        total += k - start

total += 53 * (INPUT - 195)
print(total)