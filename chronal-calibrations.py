with open('chronal-calibrations-input.txt', 'r') as file:
    sum = 0
    for line in file:
        sum = sum + int(line)
    print(sum)