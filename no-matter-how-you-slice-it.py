with open('nmhysi-input.txt', 'r') as file:
    mat_width = 1000
    mat = [[0 for _ in range(mat_width)] for _ in range(mat_width)]
    for line in file:
        sx, sy = line[line.find('@')+2: line.find(':')].split(',')
        wx, wy = line[line.find(':')+2:].split('x')
        sx = int(sx)
        sy = int(sy)
        wx = int(wx)
        wy = int(wy)
        for x in range(sx, sx+wx):
            for y in range(sy, sy+wy):
                mat[x][y] = mat[x][y] + 1
    inches = 0
    for i in range(mat_width):
        for j in range(mat_width):
            if mat[i][j] > 1:
                inches = inches + 1
    print(inches)