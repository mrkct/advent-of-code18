SERIAL = 1133

def get_power_level(serial, x, y):
  rack_id = x + 10
  power_level = ((rack_id * y) + serial) * rack_id
  power_level = int(power_level / 100) % 10
  return power_level - 5

def calculate_square_level(matrix, x, y):
  if x + 2 >= len(matrix) or y + 2 >= len(matrix):
    return 0
  total = 0
  for i in range(x, x+3):
    for j in range(y, y+3):
      total += matrix[i][j]
  return total

mat = [[0 for _ in range(300)] for _ in range(300)]

for i in range(len(mat)):
  for j in range(len(mat)):
    mat[i][j] = get_power_level(SERIAL, i+1, j+1)

best_square_level = calculate_square_level(mat, 0, 0)
position = (1, 1)
for i in range(len(mat)):
  for j in range(len(mat)):
    square_level = calculate_square_level(mat, i, j)
    if square_level > best_square_level:
      best_square_level = square_level
      position = (i+1, j+1)

print("Best square power level: {} at {}".format(best_square_level, position))