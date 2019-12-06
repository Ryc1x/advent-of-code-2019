def p1():
    s = 0
    with open("input.txt") as f:
        for line in f:
            num = int(line)
            s += num // 3 - 2
    print(s)

def p2():
    s = 0
    with open("input.txt") as f:
        for line in f:
            num = int(line)
            num = num // 3 - 2
            while num > 0:
                s += num
                num = num // 3 - 2
    print(s)