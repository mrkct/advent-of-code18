found = False
past_calibrations = set([])
sum = 0
while not found:    
    with open('chronal-calibration-input.txt', 'r') as file:
        for line in file:
            sum = sum + int(line)
            if sum in past_calibrations:
                found = True
                print(sum)
                break
            else:
                past_calibrations.add(sum)