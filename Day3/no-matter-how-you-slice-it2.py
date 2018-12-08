with open('nmhysi-input.txt', 'r') as file: # nmhysi-input.txt
    claims = []
    mat_width = 1000
    mat = [[0 for _ in range(mat_width)] for _ in range(mat_width)]
    for line in file:
        id = line[1:line.find('@')]
        x, y = line[line.find('@')+2: line.find(':')].split(',')
        width, height = line[line.find(':')+2:].split('x')
        claim = dict(
            id=id,
            x=int(x),
            y=int(y),
            width=int(width),
            height=int(height)
        )
        claims.append(claim)
        for x in range(claim['x'], claim['x'] + claim['width']):
            for y in range(claim['y'], claim['y'] + claim['height']):
                mat[x][y] = mat[x][y] + 1
    
    for claim in claims:
        overlap = False
        for x in range(claim['x'], claim['x'] + claim['width']):
            for y in range(claim['y'], claim['y'] + claim['height']):
                if mat[x][y] > 1:
                    overlap = True
                    break
        if not overlap:
            print(claim['id'])
        