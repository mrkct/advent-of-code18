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

seconds = 0

while True:
    seconds += 1
    for point in data:
        point['x'] += point['h']
        point['y'] += point['v']

    min_y = min(data, key=lambda p: p['y'])['y']
    max_y = max(data, key=lambda p: p['y'])['y']

    if max_y - min_y < 10:
        break

print(seconds)