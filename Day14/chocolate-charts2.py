INPUT = "509671"
INPUT = [int(x) for x in INPUT]

def recipies_step(recipies, current_recipies):
    v = recipies[ current_recipies[0] ] + recipies[ current_recipies[1] ]
    if v >= 10:
        recipies.append(v // 10)
    recipies.append(v % 10)

    current_recipies[0] += 1 + recipies[ current_recipies[0] ]
    current_recipies[1] += 1 + recipies[ current_recipies[1] ]
    current_recipies[0] %= len(recipies)
    current_recipies[1] %= len(recipies)

current_recipies = [0, 1]
recipies = [3, 7]

while True:
    recipies_step(recipies, current_recipies)
    if recipies[-len(INPUT):] == INPUT:
        print( len(recipies) - len(INPUT) )
        break
    if recipies[-len(INPUT)-1:-1] == INPUT:
        print( len(recipies) - len(INPUT) - 1 )
        break