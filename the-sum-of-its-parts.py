requirements = {}
with open('the-sum-of-its-parts-input.txt', 'r') as file:
    for line in file:
        required_letter, letter = line[5:6], line[36:37] # easy parsing
        if letter not in requirements:
            requirements[letter] = []
        if required_letter not in requirements: # to handle the first letter, that only appears as required
            requirements[required_letter] = []
        requirements[letter].append(required_letter)

order = ''
while requirements: # requirements has at least 1 key
    letter = 'Z'
    for l in requirements:
        if requirements[l] == [] and l <= letter:
            letter = l
    
    del requirements[letter]
    for ch in requirements:
        if letter in requirements[ch]:
            del requirements[ch][requirements[ch].index(letter)]
    
    order += letter

print(order)