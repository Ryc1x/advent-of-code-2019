# Reference: https://github.com/sophiebits/adventofcode/blob/master/2019/day5.py

def process(arr):
    ip = 0

    arity = {99: 0, 1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3}
    def parse():
        nonlocal ip
        op = arr[ip]
        ip += 1
        vals = []
        locs = []
        for i in range(arity[op % 100]):
            mode = (op // (10 ** (2 + i))) % 10
            vals.append(arr[ip] if mode == 1 else arr[arr[ip]])
            locs.append(None if mode == 1 else arr[ip])
            ip += 1
        return op % 100, vals, locs


    while arr[ip] != 99:
        op, vals, locs = parse()

        if op == 1:
            arr[locs[2]] = vals[0] + vals[1]
        elif op == 2:
            arr[locs[2]] = vals[0] * vals[1]
        elif op == 3:
            arr[locs[0]] = int(input('The computer need an input: '))
        elif op == 4:
            print('The computer outputs:', vals[0])
        elif op == 5:
            ip = vals[1] if vals[0] != 0 else ip
        elif op == 6:
            ip = vals[1] if vals[0] == 0 else ip
        elif op == 7:
            arr[locs[2]] = int(vals[0] < vals[1])
        elif op == 8:
            arr[locs[2]] = int(vals[0] == vals[1])
        else:
            assert False
    
    return arr[0]

if __name__ == "__main__":
    with open('input.txt') as f:
        s = f.readline()
        arr = [int(x) for x in s.split(',')]
        print(process(arr))