# this solution is a bit slow (about 10 sec to calculate on my machine)

def manhattan(coordinate1, coordinate2):
    return abs(coordinate1[0] - coordinate2[0]) + abs(coordinate1[1] - coordinate2[1])


def printmat(mat):
    global coordinates
    for y in range(len(mat[0])):
        for x in range(len(mat)):
            coordinate = mat[x][y]
            if coordinate is None:
                print("(None) ", end='')
            else:
                if (x, y) in coordinates:
                    print("[{}, {}] ".format(x, y), end='')
                else:
                    print("{} ".format(coordinate), end='')
        print("")


def cman(c):
    print("Printing manhattan for {}".format(c))
    for coord in coordinates:
        print("{} ==> {}".format(coord, manhattan(coord, c)))


def touches_borders(coord):
    if coord is None:
        return True
    global mat
    for x in range(len(mat)):
        if mat[x][0] == coord or mat[x][len(mat[0])-1] == coord:
            return True
    for y in range(len(mat[0])):
        if mat[0][y] == coord or mat[len(mat)-1][y] == coord:
            return True
    
    return False

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

maxCoord = (maxCoord[0]+1, maxCoord[1]+1)
mat = [[None for _ in range(maxCoord[1])] for _ in range(maxCoord[0])]
areas_count = {}


for x in range(len(mat)):
    for y in range(len(mat[0])):
        closest = coordinates[0]
        for coordinate in coordinates[1:]:
            if manhattan(coordinate, (x, y)) < manhattan(closest, (x, y)):
                closest = coordinate
        
        closest_appearances = 0
        for coordinate in coordinates:
            if manhattan(coordinate, (x, y)) == manhattan(closest, (x, y)):
                closest_appearances += 1
        if closest_appearances > 1:
            closest = None

        mat[x][y] = closest
        if closest not in areas_count:
            areas_count[closest] = 1
        else:
            areas_count[closest] += 1

best_area = 0 # no point can have less than 1 area anyway
for key in areas_count:
    if areas_count[key] > best_area and not touches_borders(key):
        best_area = areas_count[key]

print(best_area)