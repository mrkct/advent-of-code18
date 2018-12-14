INPUT = 509671

def print_recipies(recipies, current_recipies) -> None:
    for i, recipe in enumerate(recipies):
        if i == current_recipies[0]:
            print("({}) ".format(recipe), end='')
        elif i == current_recipies[1]:
            print("[{}] ".format(recipe), end='')
        else:
            print("{}  ".format(recipe), end='')

def recipies_step(recipies, current_recipies):
    recipies += [ int(x) for x in str(recipies[ current_recipies[0] ] + recipies[ current_recipies[1] ]) ]
    current_recipies[0] = ( current_recipies[0] + 1 + recipies[current_recipies[0]] ) % len(recipies)
    current_recipies[1] = ( current_recipies[1] + 1 + recipies[current_recipies[1]] ) % len(recipies)

current_recipies = [0, 1]
recipies = [3, 7]

while len(recipies) < INPUT + 10:
    recipies_step(recipies, current_recipies)

for r in recipies[INPUT:INPUT+10]:
    print(r, end='')
print('')