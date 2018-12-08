import string


def reacts(char1, char2):
    return char1.lower() == char2.lower() and char1 != char2

def get_polymer_reaction_length(polymer):
    i = 0
    while i < len(polymer)-1:
        if reacts(polymer[i], polymer[i+1]):
            del polymer[i: i+2]
            i = max(0, i-1)
        else:
            i += 1
    
    return len(polymer)

with open('alchemical-reduction-input.txt', 'r') as file:
    polymer = file.read()
    pass

polymer = list(polymer) # using a string causes OutOfMemory when you remove characters

shortest_polymer_length = 99999999
for character in string.ascii_lowercase:
    polymer_length = get_polymer_reaction_length([x for x in polymer if x.lower() != character])
    if polymer_length < shortest_polymer_length:
        shortest_polymer_length = polymer_length

print(shortest_polymer_length)