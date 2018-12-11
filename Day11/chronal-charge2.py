SERIAL = 1133

def get_power_level(serial, x, y):
    rack_id = x + 10
    power_level = ((rack_id * y) + serial) * rack_id
    power_level = (power_level // 100) % 10
    return power_level - 5

def find_best_square(matrix, size):
    square, best = None, 0
    for i in range(1, len(matrix)-size):
        for j in range(1, len(matrix)-size):
            value = mat[i+size][j+size] - mat[i][j+size] - mat[i+size][j] + mat[i][j]
            if value > best:
                best = value
                # +1 because the indexes start from 1 in the game
                # another +1 because idk, but it is needed
                square = (2 + i, 2 + j)
    return square, best


mat = [[0 for _ in range(300)] for _ in range(300)]

for i in range(len(mat)):
    for j in range(len(mat)):
        mat[i][j] = get_power_level(SERIAL, i+1, j+1)

for i in range(1, len(mat)):
    for j in range(1, len(mat)):
        mat[i][j] = mat[i][j] + mat[i-1][j] + mat[i][j-1] - mat[i-1][j-1]

best_square, best_value, best_size = None, 0, 0
for size in range(1, 300):
    square, value = find_best_square(mat, size)
    if value > best_value:
        best_value = value
        best_square = square
        best_size = size

print(best_square, best_size)