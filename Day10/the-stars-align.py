data = []

with open('the-stars-align-input.txt', 'r') as file:
    for line in file:
        x, y = [int(x) for x in line[10:line.index('>')].split(',')]
        p = line.index('<')+1
        l = line[line.index('<', p)+1: line.index('>', line.index('<', p))]
        h, v = [int(v) for v in l.split(',')]
        data.append(dict(
            x=x,
            y=y,
            h=h,
            v=v
        ))

while True:
    for point in data:
        point['x'] += point['h']
        point['y'] += point['v']

    min_y = min(data, key=lambda p: p['y'])['y']
    max_y = max(data, key=lambda p: p['y'])['y']

    if max_y - min_y < 10:
        break


min_y = min(data, key=lambda p: p['y'])['y']
min_x = min(data, key=lambda p: p['x'])['x']
max_x = max(data, key=lambda p: p['x'])['x']

mat = [['.' for _ in range(15)] for _ in range(min_x, max_x+1)]

for point in data:
    mat_x = point['x'] - min_x
    mat_y = point['y'] - min_y
    mat[mat_x][mat_y] = '#'

for j in range(len(mat[0])):
    for i in range(len(mat)):
        print(mat[i][j], end='')
    print("")
