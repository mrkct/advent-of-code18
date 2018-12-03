repeated_twos = 0
repeated_threes = 0
with open('inventory-managment-input.txt', 'r') as file:
    for line in file:
        letters = {}
        for c in line:
            if c not in letters:
                letters[c] = 1
            else:
                letters[c] = letters[c] + 1
        repeated_twos_new = two_repeated
        repeated_threes_new = three_repeated
        for key in letters:
            if letters[key] == 2:
                two_repeated_new = two_repeated + 1
            if letters[key] == 3:
                three_repeated_new = three_repeated + 1
        two_repeated = two_repeated_new
        three_repeated = three_repeated_new

print(two_repeated * three_repeated)