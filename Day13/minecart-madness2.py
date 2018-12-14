track = []
carts = []
for line in open('minecart-madness-input.txt', 'r'):
    track.append(list(line))

id = 0
for y in range(len(track)):
    for x in range(len(track[y])):
        if track[y][x] in ['<', '>', '^', 'v']:
            carts.append(dict(
                id=id,
                direction=track[y][x],
                x=x,
                y=y,
                cross=0,
                crashed=False
            ))
            id += 1
            if track[y][x] == '<' or track[y][x] == '>':
                track[y][x] = '-'
            elif track[y][x] == '^' or track[y][x] == 'v':
                track[y][x] = '|'

movements = {
    '>': (1, 0),
    '^': (0, -1),
    'v': (0, 1),
    '<': (-1, 0)
}

track_movements = {
    '\\': {
        '<': '^',
        '>': 'v',
        'v': '>',
        '^': '<'
    },
    '/': {
        '<': 'v',
        '>': '^',
        'v': '<',
        '^': '>'
    },
    '+': {
        '<': ['v', '<', '^'],
        '>': ['^', '>', 'v'],
        '^': ['<', '^', '>'],
        'v': ['>', 'v', '<']
    },
    '-': {
        '<': '<',
        '>': '>'
    },
    '|': {
        '^': '^',
        'v': 'v'
    }
}


while len(carts) > 1:
    carts.sort(key=lambda c: (c['y'], c['x']))
    for i in range(len(carts)):
        cart = carts[i]
        if cart['crashed']:
            continue
        cart['x'] += movements[cart['direction']][0]
        cart['y'] += movements[cart['direction']][1]
        track_tile = track[cart['y']][cart['x']]
        if track_tile == '+':
            cart['direction'] = track_movements[track_tile][cart['direction']][cart['cross']]
            cart['cross'] = ( cart['cross'] + 1 ) % 3
        else:
            cart['direction'] = track_movements[track_tile][cart['direction']]

        for checkcart in carts:
            if checkcart['id'] != cart['id'] and checkcart['x'] == cart['x'] and checkcart['y'] == cart['y'] and not checkcart['crashed']:
                checkcart['crashed'] = True
                cart['crashed'] = True
                break
    carts = [cart for cart in carts if not cart['crashed']]

print("{},{}".format(carts[0]['x'], carts[0]['y']))