def reacts(char1, char2):
    return char1.lower() == char2.lower() and char1 != char2

polymer = "dabAcCaCBAcCcaDA"
with open('alchemical-reduction-input.txt', 'r') as file:
    polymer = file.read()
    pass

polymer = list(polymer) # using a string causes OutOfMemory when you remove characters

i = 0
while i < len(polymer)-1:
    if reacts(polymer[i], polymer[i+1]):
        del polymer[i: i+2]
        i = max(0, i-1)
    else:
        i += 1


print(len(polymer))