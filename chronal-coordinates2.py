def manhattan(coordinate1, coordinate2):
    return abs(coordinate1[0] - coordinate2[0]) + abs(coordinate1[1] - coordinate2[1])

coordinates = []
maxCoord = (0, 0)
with open('chronal-coordinates-input.txt', 'r') as file: #chronal-coordinates-input
    for line in file:
        x, y = [int(x) for x in line.split(',')]
        coordinates.append((x, y))
        if x > maxCoord[0]:
            maxCoord = (x, maxCoord[1])
        if y > maxCoord[1]:
            maxCoord = (maxCoord[0], y)

total_area = 0
for x in range(maxCoord[0]+1):
    for y in range(maxCoord[1]+1):
        tsum = sum([manhattan(coord, (x, y)) for coord in coordinates])
        if tsum < 10000:
            total_area += 1

print(total_area)