def path1(arr):
    path = set()
    x, y = 0, 0
    for s in arr:
        direction, step = s[0], int(s[1:])
        if direction == 'L':
            dx, dy = -1, 0
        elif direction == 'R':
            dx, dy = 1, 0
        elif direction == 'U':
            dx, dy = 0, -1
        elif direction == 'D':
            dx, dy = 0, 1
        else:
            assert False

        for _ in range(step):
            x += dx
            y += dy
            path.add((x,y))

    return path

def path2(arr):
    i = 0
    records = {}
    path = set()
    x, y = 0, 0
    for s in arr:
        direction, step = s[0], int(s[1:])
        if direction == 'L':
            dx, dy = -1, 0
        elif direction == 'R':
            dx, dy = 1, 0
        elif direction == 'U':
            dx, dy = 0, -1
        elif direction == 'D':
            dx, dy = 0, 1
        else:
            assert False

        for _ in range(step):
            i += 1
            x += dx
            y += dy
            if (x,y) not in records:
                records[(x,y)] = i
            path.add((x,y))

    return path, records

if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()
    # Part 1
    p1 = path1(lines[0].split(','))
    p2 = path1(lines[1].split(','))
    intersections = p1 & p2
    print(min(abs(x)+abs(y) for (x, y) in intersections))

    # Part 2
    p1, r1 = path2(lines[0].split(','))
    p2, r2 = path2(lines[1].split(','))
    intersections = p1 & p2
    print(min([r1[(x,y)]+r2[(x,y)] for (x,y) in intersections]))
